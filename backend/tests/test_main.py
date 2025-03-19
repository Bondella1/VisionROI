import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fastapi.testclient import TestClient
import pytest
import main
from simulate_data import ROIProject as Project
# Define a simple in-memory mock container.
class MockContainer:
    def __init__(self):
        # Store items by their id in a dictionary.
        self.items = {}
    
    def create_item(self, item):
        self.items[item["id"]] = item
        return item
    
    def query_items(self, query, parameters=None, **kwargs):
        project_id = None
        if parameters:
            for param in parameters:
                if param["name"] == "@project_id":
                    project_id = param["value"]
                    break
        else:
            # If no parameters, try to extract project_id from the query string.
            # Assumes query is in the format:
            # "SELECT * FROM c WHERE c.project_id = 'TP006'"
            try:
                project_id = query.split("'")[1]
            except IndexError:
                project_id = None
        return [item for item in self.items.values() if item["project_id"] == project_id]
    
    def read_all_items(self):
        return list(self.items.values())
    
    def replace_item(self, item_id, body):
        if item_id in self.items:
            self.items[item_id] = body
            return body
        raise Exception("Item not found")
    
    def delete_item(self, item_id, partition_key):
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise Exception("Item not found")

# Use a pytest fixture to patch the 'container' in your main module.
@pytest.fixture(autouse=True)
def mock_container(monkeypatch):
    mock = MockContainer()
    monkeypatch.setattr(main, "container", mock)

client = TestClient(main.app)

def test_create_project():
    payload = {
        "id": "test_proj_1",
        "project_id": "TP001",
        "name": "Test Project",
        "initial_investment": 100000.0,
        "operating_costs": [5000, 6000],
        "expected_revenue": [15000, 16000],
        "duration_months": 12,
        "roi": 20.5
    }
    response = client.post("/projects/", json=payload)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["project_id"] == payload["project_id"]

def test_get_project():
    # Create a project first
    payload = {
        "id": "test_proj_2",
        "project_id": "TP002",
        "name": "Second Project",
        "initial_investment": 80000.0,
        "operating_costs": [4000, 5000],
        "expected_revenue": [12000, 13000],
        "duration_months": 12,
        "roi": 15.0
    }
    client.post("/projects/", json=payload)
    response = client.get("/projects/TP002")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["project_id"] == "TP002"

def test_get_project_not_found():
    response = client.get("/projects/INVALID")
    assert response.status_code == 404

def test_get_all_projects():
    # Create two projects
    payload1 = {
        "id": "test_proj_3",
        "project_id": "TP003",
        "name": "Third Project",
        "initial_investment": 90000.0,
        "operating_costs": [4500, 5500],
        "expected_revenue": [11000, 12000],
        "duration_months": 12,
        "roi": 18.0
    }
    payload2 = {
        "id": "test_proj_4",
        "project_id": "TP004",
        "name": "Fourth Project",
        "initial_investment": 95000.0,
        "operating_costs": [4600, 5600],
        "expected_revenue": [11500, 12500],
        "duration_months": 12,
        "roi": 19.0
    }
    client.post("/projects/", json=payload1)
    client.post("/projects/", json=payload2)
    response = client.get("/projects/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2

def test_update_project():
    # Create a project first
    payload = {
        "id": "test_proj_5",
        "project_id": "TP005",
        "name": "Fifth Project",
        "initial_investment": 100000.0,
        "operating_costs": [5000, 6000],
        "expected_revenue": [15000, 16000],
        "duration_months": 12,
        "roi": 20.5
    }
    client.post("/projects/", json=payload)
    # Update the project with new data
    update_payload = {
        "id": "test_proj_5",
        "project_id": "TP005",
        "name": "Updated Fifth Project",
        "initial_investment": 110000.0,
        "operating_costs": [5500, 6500],
        "expected_revenue": [15500, 16500],
        "duration_months": 12,
        "roi": 22.0
    }
    response = client.put("/project/TP005", json=update_payload)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Updated Fifth Project"

def test_delete_project():
    # Create a project to delete
    payload = {
        "id": "test_proj_6",
        "project_id": "TP006",
        "name": "Sixth Project",
        "initial_investment": 105000.0,
        "operating_costs": [5200, 6200],
        "expected_revenue": [15200, 16200],
        "duration_months": 12,
        "roi": 21.0
    }
    client.post("/projects/", json=payload)
    response = client.delete("/projects/TP006")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "Project deleted successfully"
