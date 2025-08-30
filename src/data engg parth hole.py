# -------------------------------
# Healthcare Data Analysis (Mini Project)
# -------------------------------

# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load and Clean Data
# -------------------------------
# Load dataset
df = pd.read_csv("healthcare_dataset_1500.csv")

# Remove duplicate and missing records
df = df.drop_duplicates()
df = df.dropna()

# -------------------------------
# 2. Basic Insights
# -------------------------------

# Total revenue from hospital bills
total_revenue = df["Bill_Amount"].sum()

# Most common diagnosis
common_diagnosis = df["Diagnosis"].value_counts().idxmax()

# Department with highest patients
top_department = df["Department"].value_counts().idxmax()

# Region with most patients
top_region = df["Region"].value_counts().idxmax()

# Age group analysis
df["Age_Group"] = pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, 90],
                         labels=["Child", "Teen", "Young Adult", "Adult", "Senior"])
age_distribution = df["Age_Group"].value_counts()

# Prepare summary table
summary = pd.DataFrame({
    "Total Revenue (₹)": [total_revenue],
    "Most Common Diagnosis": [common_diagnosis],
    "Top Department": [top_department],
    "Top Region": [top_region]
})

# Print insights
print("===== Healthcare Data Insights =====")
print(summary.to_string(index=False))

print("\n===== Age Group Distribution =====")
print(age_distribution.to_string())

# -------------------------------
# 3. Visualization
# -------------------------------
sns.set_theme(style="whitegrid", palette="deep")

# (A) Revenue by Department
dept_revenue = df.groupby("Department")["Bill_Amount"].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=dept_revenue, x="Department", y="Bill_Amount")
plt.title("Revenue by Department", fontsize=14, weight="bold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# (B) Patient Count by Diagnosis
diag_count = df["Diagnosis"].value_counts().reset_index()
diag_count.columns = ["Diagnosis", "Count"]

plt.figure(figsize=(8, 5))
sns.barplot(data=diag_count, x="Diagnosis", y="Count")
plt.title("Most Common Diagnoses", fontsize=14, weight="bold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# (C) Patient Distribution by Region
region_count = df["Region"].value_counts().reset_index()
region_count.columns = ["Region", "Patients"]

plt.figure(figsize=(6, 5))
sns.barplot(data=region_count, x="Region", y="Patients")
plt.title("Patient Distribution by Region", fontsize=14, weight="bold")
plt.tight_layout()
plt.show()

# (D) Age Group Distribution
plt.figure(figsize=(6, 5))
sns.barplot(x=age_distribution.index, y=age_distribution.values)
plt.title("Age Group Distribution", fontsize=14, weight="bold")
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()
