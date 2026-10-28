#Convert Total Expenditure (in rs) to Total Expenditure (in La rs)
import pandas as pd

# Load the CSV file
df = pd.read_csv("Updated_Project_Expenditure.csv")

# Identify the last column name
last_col_name = df.columns[-1]

# Convert the last column (Rs) to Lakhs
df["Total Expenditure (in La)"] = df[last_col_name] / 100000  # Divide by 1,00,000

# Save the modified CSV file
df.to_csv("Final_Updated_Project_Expenditure.csv", index=False)

print("New column 'Total Expenditure (in La)' added and file saved as 'Final_Updated_Project_Expenditure.csv'")
