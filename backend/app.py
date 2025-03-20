import os
from dotenv import load_dotenv
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from flask_cors import CORS
import plotly.express as px

# Import the Cosmos DB container from your cosmos module
from cosmos import container
# Import ROIProject from your simulate_data module (this model includes the ROI calculation)
from simulate_data import ROIProject

# Load environment variables from .env
load_dotenv()

def fetch_projects():
    """
    Query Cosmos DB for all ROI project documents and use the ROIProject model
    to ensure data integrity and calculate ROI.
    """
    query = "SELECT * FROM c"
    try:
        items = list(container.query_items(query=query, enable_cross_partition_query=True))
    except Exception as e:
        print(f"Error querying Cosmos DB: {e}")
        items = []

    projects = []
    for item in items:
        try:
            # Use the model to validate and (re)calculate ROI
            project = ROIProject(**item)
            project.calculate_roi()
            projects.append(project.model_dump())
        except Exception as e:
            print(f"Error processing project {item.get('id')}: {e}")
    return projects

# Retrieve projects from Cosmos DB
data = fetch_projects()

# Create a DataFrame from the data; if no data exists, create an empty DataFrame with the expected columns.
if data:
    df = pd.DataFrame(data)
else:
    df = pd.DataFrame(columns=["id", "project_id", "name", "initial_investment", "operating_costs", "expected_revenue", "duration_months", "roi"])

# Create a bar chart of ROI by project name.
fig = px.bar(
    df,
    x="name",
    y="roi",
    title="ROI Percentage per Project",
    labels={"roi": "ROI (%)", "name": "Project Name"}
)

# Initialize the Dash app.
app = dash.Dash(__name__,
                requests_pathname_prefix="/",
                routes_pathname_prefix="/")
app.title = "ROI Calculator Dashboard"

# Define the layout.
app.layout = html.Div([
    html.H1("ROI Calculator Dashboard"),
    dcc.Graph(id="roi-chart", figure=fig),
    html.Hr(),
    html.Div("Select a project to view details:"),
    dcc.Dropdown(
        id="project-dropdown",
        options=[{"label": row["name"], "value": row["id"]} for index, row in df.iterrows()],
        value=df.iloc[0]["id"] if not df.empty else None
    ),
    html.Div(id="project-details")
])

# Callback to display detailed information for the selected project.
@app.callback(
    Output("project-details", "children"),
    Input("project-dropdown", "value")
)
def display_project_details(selected_id):
    if df.empty:
        return html.Div("No project data available.")
    # Filter the DataFrame for the selected project.
    project = df[df["id"] == selected_id].iloc[0]
    details = html.Div([
        html.H3(project["name"]),
        html.P(f"Initial Investment: ${project['initial_investment']:,}"),
        html.P(f"Total Operating Costs: ${sum(project['operating_costs']):,}"),
        html.P(f"Total Expected Revenue: ${sum(project['expected_revenue']):,}"),
        html.P(f"ROI: {project['roi']:.2f}%"),
        html.P(f"Duration: {project.get('duration_months', 'N/A')} months")
    ])
    return details

def add_security_headers(response):
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; frame-resources 'self' http://react-domain"
    ) 

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8050)

CORS(app.server, origins=["react-domain"])
