#Group treasury receipt data by states and sum up the treasury reciept values into total treasury reciept
import pandas as pd

# Load the CSV file
file_path = "Treasury Reciept.csv"
df = pd.read_csv(file_path)

# Group by 'State Name' and sum the 'Treasury Reciept' values
df_grouped = df.groupby('State Name', as_index=False)['Treasury Reciept'].sum()

# Rename the column for clarity
df_grouped.rename(columns={'Treasury Reciept': 'Total Treasury Receipt'}, inplace=True)

# Save the result to a new CSV file (optional)
df_grouped.to_csv("Total_Treasury_Receipt.csv", index=False)

# Display the result
print(df_grouped.head())
