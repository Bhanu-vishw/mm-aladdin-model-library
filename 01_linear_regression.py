"""
Model Name: Linear Regression
Required Columns: ["feature1", "feature2", "target"]
Input Format: CSV
Description: Fits y = a + b1*feature1 + b2*feature2.
"""
import sys
import pandas as pd
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 3:
    print("Usage: python 01_linear_regression.py <input_csv> <output_file>")
    sys.exit(1)

input_csv = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_csv)
X = df[["feature1", "feature2"]]
y = df["target"]

model = LinearRegression()
model.fit(X, y)

with open(output_file, "w") as f:
    f.write(f"Intercept: {model.intercept_}\n")
    f.write(f"Coefficients: {model.coef_}\n")
