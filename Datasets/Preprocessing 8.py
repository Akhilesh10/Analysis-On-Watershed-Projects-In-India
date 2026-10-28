#Convert Total Treasury Reciept (in rs) to Total Treasury Reciept (in la rs)
import pandas as pd

# Load the provided CSV file
file_path = "Total_Treasury_Receipt.csv"
df = pd.read_csv(file_path)

# Create a new column converting the amount into lakhs
df["Total Treasury Receipt (in Lakhs)"] = df["Total Treasury Receipt"] / 100000

# Save the updated file
updated_file_path = "Total_Treasury_Receipt_Updated.csv"
df.to_csv(updated_file_path, index=False)

# Display the first few rows
print(df.head())
