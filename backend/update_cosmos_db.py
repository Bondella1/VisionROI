from azure.cosmos import CosmosClient, exceptions
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = os.getenv("DATABASE_NAME")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

if not DATABASE_NAME:
    raise ValueError("DATABASE_NAME is not set in your environment variables. Please check your .env file.")


# Assume you've already loaded your environment variables and set up the client, database, and container.
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

def update_missing_project_date():
    # Query for documents missing the "project_date" field
    query = "SELECT * FROM c WHERE NOT IS_DEFINED(c.project_date)"
    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    
    print(f"Found {len(items)} documents missing 'project_date'.")
    
    for item in items:
        # Define a default project_date or compute it as needed
        # Here we simply set it to the current date and time.
        item["project_date"] = datetime.now().isoformat()
        try:
            container.replace_item(item=item["id"], body=item)
            print(f"Updated document with id: {item['id']}")
        except exceptions.CosmosHttpResponseError as e:
            print(f"Error updating document {item['id']}: {e.message}")

if __name__ == "__main__":
    update_missing_project_date()
