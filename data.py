# -------------------------------
# Project 1: Data Cleaning & Exploration
# Dataset: Netflix Movies and TV Shows (CSV)
# -------------------------------

import pandas as pd

# --- CHANGE THIS PATH if your CSV is somewhere else ---
file_path = r"C:\Users\hamza\Documents\Further Studies\Computer science\Netflix\netflix_titles.csv"

# Load CSV
df = pd.read_csv(file_path)
print("Dataset loaded successfully!\n")

# ----- Basic Overview -----
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nFirst 5 rows:")
print(df.head())

# ----- Check Missing Values -----
print("\nMissing Values:")
print(df.isnull().sum())

# ----- Handle Missing Data -----
if 'country' in df.columns:
    df["country"].fillna("Unknown", inplace=True)
if 'director' in df.columns:
    df.dropna(subset=["director"], inplace=True)

# ----- Remove Duplicates -----
before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print(f"\nRemoved {before - after} duplicate rows.")

# ----- Basic Statistics -----
if 'release_year' in df.columns:
    print("\nRelease Year Summary:")
    print(df["release_year"].describe())

# ----- Most Common Categories/Genres -----
if 'listed_in' in df.columns:
    print("\nMost Common Categories:")
    print(df["listed_in"].value_counts().head(10))

# ----- Save Cleaned Data -----
cleaned_file_path = r"C:\Users\hamza\Documents\Further Studies\Computer science\Netflix\netflix_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved as {cleaned_file_path}")

print("\n--- Cleaning Complete ---")

