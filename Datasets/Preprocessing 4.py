#Converted Datatype of Project sanction date from string to dattime format
import pandas as pd

# Load the CSV file
df = pd.read_csv("Final_Merged_State_DOSP.csv")  

# Convert 'Project Sanction Date' to datetime format
df["Project Sanction Date"] = pd.to_datetime(df["Project Sanction Date"], format="%d-%m-%Y", errors="coerce")

# Get updated column data types and non-null counts
df.info()

# Save the cleaned file
df.to_csv("Cleaned_Final_Merged_State_DOSP.csv", index=False)

print("Date columns formatted and saved as 'Cleaned_Final_Merged_State_DOSP.csv'")
