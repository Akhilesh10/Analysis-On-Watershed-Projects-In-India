#Preprocessing- generate total projects done in each state.
import pandas as pd

# Load the dataset
file_path = "Cleaned_Final_Merged_State_DOSP.csv"  # Update with your file path
df = pd.read_csv(file_path)

# Preserve original order of states
df["State Name"] = pd.Categorical(df["State Name"], categories=df["State Name"].unique(), ordered=True)

# Count the number of projects for each state while maintaining order
state_project_counts = df.groupby("State Name").size().reset_index(name="Total Projects Done")

# Save to a new CSV file
output_path = "State_Total_Projects.csv"  # Specify your desired output file path
state_project_counts.to_csv(output_path, index=False)

print(f"CSV file saved successfully as {output_path}")
