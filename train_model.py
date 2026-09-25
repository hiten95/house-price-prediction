import pandas as pd

file_path = r"D:\Exercisee\housing.csv"

df = pd.read_csv(file_path)

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst five rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())
