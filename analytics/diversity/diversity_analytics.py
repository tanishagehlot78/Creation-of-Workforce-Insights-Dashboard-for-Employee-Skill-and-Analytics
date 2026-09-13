from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INPUT = Path("clean_workforce_dataset.xlsx")
OUTPUT = Path("diversity_outputs")
CHARTS = OUTPUT / "charts"
OUTPUT.mkdir(exist_ok=True)
CHARTS.mkdir(exist_ok=True)

df = pd.read_excel(INPUT)

# Remove exact duplicate rows and trim text fields
for c in df.select_dtypes(include="object").columns:
    df[c] = df[c].astype("string").str.strip()
df = df.drop_duplicates().reset_index(drop=True)

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
bins = [17, 25, 35, 45, 55, np.inf]
labels = ["18–25", "26–35", "36–45", "46–55", "56+"]
df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels, include_lowest=True)

def summary(col):
    out = df[col].value_counts(dropna=False).rename_axis(col).reset_index(name="Employees")
    out[col] = out[col].fillna("Unknown")
    out["Percentage"] = (out["Employees"] / len(df) * 100).round(2)
    return out

gender = summary("Gender")
age_groups = df["Age Group"].value_counts().reindex(labels, fill_value=0).rename_axis("Age Group").reset_index(name="Employees")
age_groups["Percentage"] = (age_groups["Employees"] / len(df) * 100).round(2)
department = summary("Department")

def bar(data, x, y, title, filename, rotate=0):
    ax = data.set_index(x)[y].plot(kind="bar", figsize=(9,5))
    ax.set_title(title); ax.set_xlabel(x); ax.set_ylabel("Employees")
    plt.xticks(rotation=rotate, ha="right" if rotate else "center")
    plt.tight_layout(); plt.savefig(CHARTS / filename, dpi=180); plt.close()

bar(gender, "Gender", "Employees", "Workforce Gender Distribution", "gender_distribution.png")
bar(age_groups, "Age Group", "Employees", "Workforce Age Group Distribution", "age_group_distribution.png")
bar(department, "Department", "Employees", "Employees by Department", "department_distribution.png", 20)

gender_department = pd.crosstab(df["Department"], df["Gender"]).reset_index()
age_department = df.groupby("Department")["Age"].agg(
    Employees="count", Average_Age="mean", Minimum_Age="min", Maximum_Age="max"
).reset_index()
age_department["Average_Age"] = age_department["Average_Age"].round(2)

with pd.ExcelWriter(OUTPUT / "diversity_analytics_outputs.xlsx", engine="openpyxl") as writer:
    gender.to_excel(writer, "Gender", index=False)
    age_groups.to_excel(writer, "Age_Groups", index=False)
    department.to_excel(writer, "Department", index=False)
    gender_department.to_excel(writer, "Gender_Department", index=False)
    age_department.to_excel(writer, "Age_Department", index=False)

print("Milestone 3 Diversity Analytics completed.")
