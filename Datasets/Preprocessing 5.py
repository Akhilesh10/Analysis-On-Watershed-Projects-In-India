#Add new column called "Total Expenditure", which will be the sum of columns 3, 4, 5, and 6. 
import pandas as pd

# Load the CSV file
df = pd.read_csv("Project Expenditure.csv")

# Add a new column "Total Expenditure" by summing columns 3, 4, 5, and 6
df["Total Expenditure"] = df.iloc[:, 2] + df.iloc[:, 3] + df.iloc[:, 4] + df.iloc[:, 5]

# Save the modified CSV file
df.to_csv("Updated_Project_Expenditure.csv", index=False)

print("New column 'Total Expenditure' added and file saved as 'Updated_Project_Expenditure.csv'")
