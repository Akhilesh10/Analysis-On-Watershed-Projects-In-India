import matplotlib.pyplot as plt
import numpy as np

# Data for the three clusters
clusters = ["Cluster 0\n(Inefficient Spenders)", 
            "Cluster 1\n(Slow Receivers, Efficient Spenders)", 
            "Cluster 2\n(High Performers)"]

release_efficiency = [18.27, 10.98, 30.94]
expenditure_efficiency = [46.91, 78.51, 80.16]
overall_utilization = [8.51, 8.63, 24.49]

# Define distinct colors for each cluster with a modern gradient style
cluster_colors = ["#E63946", "#457B9D", "#2A9D8F"]  # Warm Red, Cool Blue, Rich Teal

# Set bar width and positions
bar_width = 0.25
x = np.arange(len(clusters))

# Create the figure with a larger size and modern style
fig, ax = plt.subplots(figsize=(12, 7), facecolor="#F8F9FA")  # Light background

# Plot bars with gradient effect using transparency & shadow
ax.bar(x - bar_width, release_efficiency, width=bar_width, label="Release Efficiency",
       color=cluster_colors[0], alpha=0.85, edgecolor='black', linewidth=1.5, hatch='//', zorder=3)

ax.bar(x, expenditure_efficiency, width=bar_width, label="Expenditure Efficiency",
       color=cluster_colors[1], alpha=0.85, edgecolor='black', linewidth=1.5, hatch='\\\\', zorder=3)

ax.bar(x + bar_width, overall_utilization, width=bar_width, label="Overall Utilization",
       color=cluster_colors[2], alpha=0.85, edgecolor='black', linewidth=1.5, hatch='xx', zorder=3)

# Add value labels above bars with slight elevation
for i in range(len(x)):
    ax.text(x[i] - bar_width, release_efficiency[i] + 2, f"{release_efficiency[i]:.1f}%", 
            ha='center', fontsize=12, color='black', fontweight='bold', bbox=dict(facecolor="white", edgecolor="none", alpha=0.6))
    
    ax.text(x[i], expenditure_efficiency[i] + 2, f"{expenditure_efficiency[i]:.1f}%", 
            ha='center', fontsize=12, color='black', fontweight='bold', bbox=dict(facecolor="white", edgecolor="none", alpha=0.6))
    
    ax.text(x[i] + bar_width, overall_utilization[i] + 2, f"{overall_utilization[i]:.1f}%", 
            ha='center', fontsize=12, color='black', fontweight='bold', bbox=dict(facecolor="white", edgecolor="none", alpha=0.6))

# Labels and title with sleek font styles
ax.set_xticks(x)
ax.set_xticklabels(clusters, fontsize=12, fontweight='bold', color="#2C3E50")
ax.set_ylabel("Efficiency (%)", fontsize=13, fontweight='bold', color="#2C3E50")
ax.set_title("Fund Efficiency Metrics Across Clusters", fontsize=16, fontweight='bold', color="#1D3557", pad=20)

# Customize legend - move it outside and fix cutoff issue
legend = ax.legend(loc="upper left", bbox_to_anchor=(1.05, 1), fontsize=12, frameon=True, edgecolor='black')
plt.subplots_adjust(right=0.75)  # Ensures space on the right for the legend

# Add soft grid lines
ax.grid(axis='y', linestyle='dashed', alpha=0.5, zorder=0)

# Remove unnecessary borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Show the plot
plt.show()
