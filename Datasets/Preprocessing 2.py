#Preprocessing 2- Renumbered the first column (Sl.No) as it was not properly numbered till the last row of the data.
import pandas as pd

# Load the CSV file
file_path = "Merged_States_DOSP.csv"
df = pd.read_csv(file_path)

# Ensure the first column is named correctly
df.iloc[:, 0] = range(1, len(df) + 1)  # Renumbering from 1 to end

# Save the corrected file
df.to_csv("Corrected_Merged_States_DOSP.csv", index=False)

print("Serial numbers corrected and saved as 'Corrected_Merged_States_DOSP.csv'")
