import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Sample dataset (expanded to include more departments including IT)
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Finance,Africa,79.6,15,3.7
EMP002,Marketing,Europe,61.62,11,4.4
EMP003,Marketing,Middle East,88.82,13,3.5
EMP004,Sales,Africa,65.09,11,3.3
EMP005,HR,Asia Pacific,66.63,8,4.4
EMP006,IT,North America,85.5,12,4.2
EMP007,IT,Europe,78.3,9,3.9
EMP008,Finance,Asia Pacific,72.4,14,3.8
EMP009,IT,Africa,81.2,10,4.1
EMP010,Sales,Europe,69.8,7,3.6
EMP011,IT,Middle East,88.9,15,4.5
EMP012,Marketing,North America,75.6,8,4.0
EMP013,IT,Asia Pacific,82.7,11,4.3
EMP014,HR,Europe,70.5,6,3.7
EMP015,Finance,Middle East,76.3,13,3.9
EMP016,IT,Africa,79.8,9,4.0
EMP017,Sales,Asia Pacific,68.4,10,3.5
EMP018,IT,Europe,84.2,14,4.4
EMP019,Marketing,Africa,71.9,7,3.8
EMP020,IT,North America,87.5,16,4.6"""

# Load the data
df = pd.read_csv(StringIO(data))

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