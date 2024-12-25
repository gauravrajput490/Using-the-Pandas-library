import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
data = pd.read_csv('data.csv')

# Basic Data Analysis
print("Data Overview:")
print(data.head())

# Calculate the average of a selected column
avg_salary = data['Salary'].mean()
print(f"\nAverage Salary: {avg_salary}")

# Visualization 1: Bar Chart (Average Salary by Department)
plt.figure(figsize=(8, 6))
avg_salary_by_dept = data.groupby('Department')['Salary'].mean()
avg_salary_by_dept.plot(kind='bar', color='skyblue')
plt.title('Average Salary by Department')
plt.ylabel('Average Salary')
plt.xlabel('Department')
plt.show()

# Visualization 2: Scatter Plot (Age vs. Salary)
plt.figure(figsize=(8, 6))
plt.scatter(data['Age'], data['Salary'], color='orange', edgecolor='k')
plt.title('Age vs. Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# Visualization 3: Heatmap (Correlation Matrix)
plt.figure(figsize=(8, 6))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Insights and Observations
print("\nInsights:")
print("- The average salary across all departments is calculated.")
print("- The bar chart shows differences in average salaries by department.")
print("- The scatter plot indicates the relationship between age and salary.")
print("- The heatmap shows the correlation between numerical columns.")

