#Preprocessing 3- Dropped last column as it was repetitive
import pandas as pd

# Load the CSV file
file_path = "Corrected_Merged_States_DOSP.csv"
df = pd.read_csv(file_path)

# Renumber the first column
df.iloc[:, 0] = range(1, len(df) + 1)  # Renumbering from 1 to end

# Drop the last column
df = df.iloc[:, :-1]

# Save the corrected file
df.to_csv("Final_Merged_State_DOSP.csv", index=False)

print("Serial numbers corrected, last column dropped, and saved as 'Final_Merged_State_DOSP.csv'")
