# week7_day2.py
# Goal: Learn how to clean and transform data using pandas

import pandas as pd

# --- 1. Load the CSV from Day 1 ---
df = pd.read_csv("health_metrics_sample.csv")

print("=== Original Data ===")
print(df)
print()

# --- 2. Introduce some fake missing data for practice ---
df.loc[1, "BloodSugar"] = None  # Set one value to NaN
df.loc[2, "Systolic"] = None
print("=== Data with Missing Values ===")
print(df)
print()

# --- 3. Check for missing data ---
print("Missing values count per column:")
print(df.isnull().sum())
print()

# --- 4. Handle missing values ---
# Option A: Fill with a default value
df_filled = df.fillna(0)
print("=== Missing Values Filled with 0 ===")
print(df_filled)
print()

# Option B: Fill with column mean (more realistic for health data)
df_mean_filled = df.fillna(df.mean(numeric_only=True))
print("=== Missing Values Filled with Mean ===")
print(df_mean_filled)
print()

# --- 5. Rename columns ---
df_renamed = df_mean_filled.rename(columns={"BloodSugar": "GlucoseLevel"})
print("=== Columns Renamed ===")
print(df_renamed.head())
print()

# --- 6. Change data types ---
df_renamed["Date"] = pd.to_datetime(df_renamed["Date"])
print("Date column type after conversion:", df_renamed["Date"].dtype)
print()

# --- 7. Filter data: only rows with Systolic > 125 ---
filtered_df = df_renamed[df_renamed["Systolic"] > 125]
print("=== Filtered Data (Systolic > 125) ===")
print(filtered_df)
print()

# --- 8. Save cleaned data to CSV ---
df_renamed.to_csv("health_metrics_cleaned.csv", index=False)
print("Cleaned CSV saved as 'health_metrics_cleaned.csv'")
