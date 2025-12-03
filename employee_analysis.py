import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Sample dataset (expanded to include more departments including IT)
# Load the data
df = pd.read_csv("emp-data.csv")

# Print dataset info
print("=" * 60)
print("EMPLOYEE PERFORMANCE ANALYSIS")
print("Email: 23f2005452@ds.study.iitm.ac.in")
print("=" * 60)
print(f"\nTotal Employees: {len(df)}")
print(f"\nDataset Preview:")
print(df.head())

# Calculate frequency count for IT department
it_count = df[df['department'] == 'IT'].shape[0]
print(f"\n{'=' * 60}")
print(f"IT DEPARTMENT FREQUENCY COUNT: {it_count}")
print(f"{'=' * 60}")

# Get department distribution
dept_counts = df['department'].value_counts()
print(f"\nDepartment Distribution:")
print(dept_counts)

# Create visualization
plt.figure(figsize=(12, 6))

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

# Create histogram
ax = sns.countplot(data=df, x='department', order=dept_counts.index)

# Customize the plot
plt.title('Employee Distribution Across Departments', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Department', fontsize=12, fontweight='bold')
plt.ylabel('Number of Employees', fontsize=12, fontweight='bold')

# Add value labels on bars
for container in ax.containers:
    ax.bar_label(container, fontsize=10, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Highlight IT department bar
for i, dept in enumerate(dept_counts.index):
    if dept == 'IT':
        ax.patches[i].set_facecolor('#FF6B6B')
        ax.patches[i].set_edgecolor('black')
        ax.patches[i].set_linewidth(2)

plt.tight_layout()

# Save the figure
plt.savefig('employee_distribution.png', dpi=300, bbox_inches='tight')
print(f"\nVisualization saved as 'employee_distribution.png'")

plt.show()

print(f"\n{'=' * 60}")
print("ANALYSIS COMPLETE")
print(f"{'=' * 60}")
