#Import libraries and load data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
# Load datasets with correct folder path
state_budget = pd.read_csv('Final Preprocessed Data/State_Total_Cost.csv')
state_projects = pd.read_csv('Final Preprocessed Data/State_Total_Projects.csv')
state_mandays_farmers = pd.read_csv('Final Preprocessed Data/Project Outcome-Farmers Benefitted.csv')


#State-Total Budget Visualization
# State-Total Budget Visualization
plt.figure(figsize=(12, 6))
sns.barplot(x='State Name', y='Total Cost', data=state_budget, palette='viridis')
plt.title('Total Budget State-wise')
plt.xlabel('State')
plt.ylabel('Total Budget (in Lakhs)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# State-Total Projects Visualization
plt.figure(figsize=(12, 6))
sns.barplot(x='State Name', y='Total Projects Done', data=state_projects, palette='magma')
plt.title('Total Projects State-wise')
plt.xlabel('State')
plt.ylabel('Total Projects')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# State-Mandays Generated and Farmers Benefitted Visualization
plt.figure(figsize=(14, 8))

# Subplot 1: Mandays Generated
plt.subplot(2, 1, 1)
sns.barplot(x='State Name', y='No. of Mandays generated (in mandays)', data=state_mandays_farmers, palette='coolwarm')
plt.title('Mandays Generated State-wise')
plt.xlabel('State')
plt.ylabel('Mandays Generated')
plt.xticks(rotation=90)

# Subplot 2: Farmers Benefitted (Stacked Bar Plot)
plt.subplot(2, 1, 2)

# Prepare data for stacked bar plot
farmers_data = state_mandays_farmers[['State Name', 'SC', 'ST', 'Others', 'Female','Small Farmers','Marginal Farmers','Landless','BPL']].set_index('State Name')

# Plot stacked bar plot
farmers_data.plot(kind='bar', stacked=True, colormap='viridis', ax=plt.gca())
plt.title('Farmers Benefitted State-wise (Breakdown by Category)')
plt.xlabel('State')
plt.ylabel('Number of Farmers Benefitted')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()