import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Step 1: Generate Sample Data
roles = ["Programmer", "Engineer", "Worker", "Manager", "Designer", "Analyst", "Technician", "HR", "Consultant"]
personalities = ["INFP", "ENFP", "ESFJ", "ISTP", "INFJ", "ENTP", "ENTJ", "ISFP", "INTP", "ESTP", "ESTJ", "ISFJ", "ISTJ", "ENFJ", "INTJ", "ESFP"]

data = {
    "Employee ID": list(range(1, 351)),
    "Name": [f"Employee_{i}" for i in range(1, 351)],
    "Role": [random.choice(roles) for _ in range(350)],
    "Personality Type": [random.choice(personalities) for _ in range(350)]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Step 2: Analyze Personality Distribution
personality_counts = df["Personality Type"].value_counts()
personality_percentages = (personality_counts / len(df)) * 100

summary_df = pd.DataFrame({
    "Personality Type": personality_counts.index,
    "Count": personality_counts.values,
    "Percentage": personality_percentages.values
})

# Step 3: Visualize the Distribution
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))
sns.barplot(x="Personality Type", y="Percentage", data=summary_df, palette="viridis")
plt.title("Personality Distribution in AequorTech CTRL by Fozan Ahmed", fontsize=16)
plt.xlabel("Personality Type", fontsize=12)
plt.ylabel("Percentage (%)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("personality_distribution.png")
plt.show()

# Step 4: Add Lookup Functions
def find_personality_by_name(name):
    employee = df[df["Name"].str.lower() == name.lower()]
    if not employee.empty:
        personality = employee.iloc[0]["Personality Type"]
        print(f"{name}'s Personality Type: {personality}")
    else:
        print(f"Employee {name} not found.")

def find_personality_by_id(emp_id):
    employee = df[df["Employee ID"] == emp_id]
    if not employee.empty:
        personality = employee.iloc[0]["Personality Type"]
        print(f"Employee ID {emp_id}'s Personality Type: {personality}")
    else:
        print(f"Employee ID {emp_id} not found.")

# Example Usage
find_personality_by_name("Employee_340")
find_personality_by_id(230)
