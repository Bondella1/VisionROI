from cosmos import container
import json
import random
from pydantic import BaseModel, Field
from typing import List, Optional
from azure.cosmos import exceptions

#pydantic model to verify dataset input
class ROIProject(BaseModel):
    id:str
    project_id:str
    name:str
    initial_investment:float
    operating_costs:List[float]
    expected_revenue:List[float]
    duration_months:int
    roi: Optional[float] = Field(None, description="Calculated Roi as a percentage")

    #roi formula calculation
    def calculate_roi(self) -> float:
        total_cost = self.initial_investment + sum(self.operating_costs)
        total_revenue = sum(self.expected_revenue)
        self.roi = ((total_revenue - total_cost) / self.initial_investment) * 100
        return self.roi

def generate_sample_project(project_id: int) -> ROIProject:
    initial_investment = random.uniform(50000, 150000)
    duration = random.randint(12, 36)
    operating_costs = [random.uniform(4000, 7000) for _ in range(duration)]
    expected_revenues = [random.uniform(8000, 12000) for _ in range(duration)]

    project = ROIProject(
        id=f"proj_{project_id}",
        project_id=f"project_id:03",
        name=f"Project {project_id}",
        initial_investment=initial_investment,
        operating_costs=operating_costs,
        expected_revenue=expected_revenues,
        duration_months=duration
    )
    project.calculate_roi()
    return project

def generate_projects(n:int) -> List[ROIProject]:
    return [generate_sample_project(i) for i in range(1, n+1)]

def main():
    projects = generate_projects(5)
    for project in projects:
        try:
            container.create_item(project.model_dump())
            print(f"Inserted: {project.project_id} with ROI: {project.roi:.2f}%")
        except exceptions.CosmosHttpResponseError as e:
            print(f"Error inserting {project.project_id}: {e.message}")

    with open('roi_sample_data.json', 'w') as f:
        json.dump([project.model_dump()for project in projects], f, indent=4)
    print("Simulation complete. Sample data generated and stored.")

if __name__ == "__main__":
    main()
    