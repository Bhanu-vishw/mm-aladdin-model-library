import sys
import pandas as pd
import numpy as np

# Usage: python script.py input.csv output.txt

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

# Expecting columns: 'S0', 'mu', 'sigma', 'T', 'N', 'M'
S0 = float(df['S0'].iloc[0])
mu = float(df['mu'].iloc[0])
sigma = float(df['sigma'].iloc[0])
T = float(df['T'].iloc[0])
N = int(df['N'].iloc[0])        # Steps
M = int(df['M'].iloc[0])        # Paths

dt = T / N
paths = np.zeros((M, N + 1))
paths[:, 0] = S0

for t in range(1, N + 1):
    z = np.random.standard_normal(M)
    paths[:, t] = paths[:, t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)

final_prices = paths[:, -1]
mean_price = np.mean(final_prices)

with open(output_file, "w") as f:
    f.write(f"Monte Carlo Estimated Final Asset Price: {mean_price:.4f}\n")
    f.write(f"All Simulated Final Prices: {final_prices.tolist()}\n")
