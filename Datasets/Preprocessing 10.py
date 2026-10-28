#Preprocessing-Generate total budget for each state
import pandas as pd

# Load the dataset
file_path = "Cleaned_Final_Merged_State_DOSP.csv"  # Update with your file path
df = pd.read_csv(file_path)

# Preserve the original order of states
df["State Name"] = pd.Categorical(df["State Name"], categories=df["State Name"].unique(), ordered=True)

# Group by state and sum the Total Cost while maintaining order
state_total_cost = df.groupby("State Name", observed=True)["Total Cost"].sum().reset_index()

# Save to a new CSV file
output_path = "State_Total_Cost.csv"
state_total_cost.to_csv(output_path, index=False)

print(f"CSV file saved successfully as {output_path}")
