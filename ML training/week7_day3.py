# week7_day3.py
# Goal: Learn Grouping, Aggregation, and Merging in Pandas

import pandas as pd

# --- 1. Load cleaned data from Day 2 ---
df = pd.read_csv("health_metrics_cleaned.csv")

print("=== Original Cleaned Data ===")
print(df)
print()

# --- 2. Add more rows for practice ---
extra_data = {
    "Date": ["2025-07-04", "2025-07-04", "2025-07-05"],
    "Systolic": [135, 128, 122],
    "Diastolic": [88, 83, 80],
    "GlucoseLevel": [102, 97, 95]
}
extra_df = pd.DataFrame(extra_data)

# Combine with original dataframe
df = pd.concat([df, extra_df], ignore_index=True)
print("=== Extended Data ===")
print(df)
print()

# --- 3. Group by Date and compute averages ---
daily_avg = df.groupby("Date").mean(numeric_only=True)
print("=== Daily Averages ===")
print(daily_avg)
print()

# --- 4. Sort by Systolic ---
sorted_df = df.sort_values(by="Systolic", ascending=False)
print("=== Sorted by Systolic (descending) ===")
print(sorted_df)
print()

# --- 5. Merge with another dataset (simulating patient info) ---
patient_info = pd.DataFrame({
    "PatientID": [1, 2, 3, 4, 5, 6],
    "Age": [45, 52, 38, 60, 41, 55]
})

# Add PatientID column to df for merging
df["PatientID"] = [1, 2, 3, 4, 5, 6]  # matches row count
merged_df = pd.merge(df, patient_info, on="PatientID")

print("=== Merged Data (Health + Patient Info) ===")
print(merged_df)
print()

# --- 6. Save grouped data ---
daily_avg.to_csv("daily_avg_metrics.csv")
print("Grouped data saved as 'daily_avg_metrics.csv'")
