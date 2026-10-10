import pandas as pd

df = pd.read_csv("insurance_operations_sample_data.csv", parse_dates=["Received_Date"])
print("Rows and columns:", df.shape)
print("\nCases by outcome:")
print(df["Outcome"].value_counts())
print("\nSLA status (%):")
print((df["SLA_Status"].value_counts(normalize=True) * 100).round(1))
print("\nAverage turnaround time by case type:")
print(df.groupby("Case_Type")["Processing_TAT_Days"].mean().round(2).sort_values(ascending=False))
print("\nCase volume by analyst:")
print(df.groupby("Assigned_Analyst")["Case_ID"].count().sort_values(ascending=False))
