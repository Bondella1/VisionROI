from azure.cosmos import CosmosClient, exceptions, PartitionKey
from dotenv import load_dotenv
import os

load_dotenv()

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT") 
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = os.getenv("DATABASE_NAME")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)

try:
    database = client.create_database_if_not_exists(DATABASE_NAME)
    print(f"Database'{DATABASE_NAME}' is ready.")
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(DATABASE_NAME)

try:
    container = database.create_container_if_not_exists(
        id=CONTAINER_NAME,
        partition_key=PartitionKey(path="/project_id")
    )
    print(f"Container '{CONTAINER_NAME}' is ready.")
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(CONTAINER_NAME)

def test_cosmos():
    test_project = {
        "id":"12345",
        "project_id": "67890",
        "name": "clientapp",
        "budget": 500000,
        "employees_impacted": 200,
        "duration_months":12,
        "roi_prediction": 150000
    }

    try:
        container.upsert_item(test_project)
        print("Test successful")
    except Exception as e:
        print(f"Error inserting projects: {e}")

#query using partition key
    query = f"SELECT * FROM c WHERE c.project_id = @project_id"
    parameters = [{"name": "@project_id", "value":test_project["project_id"]}]

    try:
        results = list(container.query_items(
            query=query,
            parameters=parameters,
            partition_key=test_project["project_id"]
        ))
        if results:
            print("Retrieved from Cosmos DB:", results[0])
        else:
            print("Project not found.")
    except exceptions.CosmosHttpResponseError as e:
        print(f"Failed to query data: {e.message}")

if __name__ == "__main__":
    test_cosmos()