from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import List, Optional
from azure.cosmos import exceptions
from cosmos import container
from simulate_data import ROIProject as Project  # Project model imported from simulate_data.py
from starlette.middleware.wsgi import WSGIMiddleware
#from app import app as dash_app

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Create a new project
@app.post("/projects/", response_model=Project)
def create_project(project: Project):
    try:
        container.create_item(project.model_dump())
        return project
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Retrieve a project by its project_id
@app.get("/projects/{project_id}", response_model=Project)
def get_project(project_id: str):
    try:
        query = f"SELECT * FROM c WHERE c.project_id = '{project_id}'"
        items = list(container.query_items(
            query=query,
            parameters=[{"name": "@project_id", "value": project_id}],
            enable_cross_partition_query=True
        ))
        if not items:
            raise HTTPException(status_code=404, detail="Project not found")
        return items[0]
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Retrieve all projects
@app.get("/projects/", response_model=List[Project])
def get_all_projects():
    try:
        items = list(container.read_all_items())
        return items
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Update a project
@app.put("/project/{project_id}", response_model=Project)
def update_project(project_id: str, project: Project):
    try:
        query = f"SELECT * FROM c WHERE c.project_id = @project_id"
        items = list(container.query_items(
            query=query,
            parameters=[{"name": "@project_id", "value": project_id}],
            enable_cross_partition_query=True
        ))
        if not items:
            raise HTTPException(status_code=404, detail="Project not found")
        project_data = project.model_dump()
        project_data["id"] = items[0]["id"]

        container.replace_item(items[0]["id"], project_data)
        return project_data
    
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete a project
@app.delete("/projects/{project_id}")
def delete_project(project_id: str):
    try:
        query = f"SELECT * FROM c WHERE c.project_id = '{project_id}'"
        items = list(container.query_items(query, enable_cross_partition_query=True))
        if not items:
            raise HTTPException(status_code=404, detail="Project not found")
        
        container.delete_item(items[0]["id"], partition_key=items[0]["project_id"])
        return {"message": "Project deleted successfully"}
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=500, detail=str(e))

#print(dash_app.server.url_map)
#app.mount("/dash/", WSGIMiddleware(dash_app.server))