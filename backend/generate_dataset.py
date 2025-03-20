import pandas as pd
from simulate_data import generate_projects

def main():
    # Set the number of projects you want to simulate
    num_samples = 1000  # For example, generate 1000 projects
    
    # Generate the projects using your simulate_data module
    projects = generate_projects(num_samples)
    
    # Convert each ROIProject instance to a dictionary
    data = [proj.model_dump() for proj in projects]
    
    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    
    # Optional: If you added a 'project_date' field, convert and sort by date
    if 'project_date' in df.columns:
        df['project_date'] = pd.to_datetime(df['project_date'])
        df.sort_values('project_date', inplace=True)
    
    # Save the DataFrame to a CSV file
    output_file = "historical_roi_data.csv"
    df.to_csv(output_file, index=False)
    print(f"Historical data generated and saved to {output_file}")

if __name__ == "__main__":
    main()
