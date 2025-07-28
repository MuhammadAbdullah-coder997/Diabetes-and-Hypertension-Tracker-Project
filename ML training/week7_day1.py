# week7_day1.py
# Goal: Learn Pandas Series & DataFrame fundamentals

import pandas as pd

#--- 1. Create a Series ---
blood_sugar_series = pd.Series([95, 100, 105, 110, 98])
print("=== Blood Sugar Series ===")
print(blood_sugar_series)
print()

#--- 2. Access elements in Series ---
print("First value:", blood_sugar_series[0])
print("Last value:", blood_sugar_series.iloc[-1])
print()

#--- 3. Create a DataFrame ---
data = {
    "Date": ["2025-07-01", "2025-07-02", "2025-07-03"],
    "Systolic": [120, 130, 125],
    "Diastolic": [80, 85, 82],
    "BloodSugar": [95, 100, 98]
}

df = pd.DataFrame(data)

print("=== Health Metrics DataFrame ===")
print(df)
print()

# --- 4. Basic DataFrame Info ---
print("DataFrame Info:")
print(df.info())
print()

print("First few rows using head():")
print(df.head())
print()

# --- 5. Select a single column ---
print("Systolic column:")
print(df["Systolic"])
print()

# --- 6. Select multiple columns ---
print("Systolic & Diastolic:")
print(df[["Systolic", "Diastolic"]])
print()

# --- 7. Filter rows where Systolic > 125 ---
high_bp = df[df["Systolic"] > 125]
print("Rows with Systolic > 125:")
print(high_bp)
print()

# --- 8. Save DataFrame to CSV ---
df.to_csv("health_metrics_sample.csv", index=False)
print("CSV file 'health_metrics_sample.csv' saved!")
