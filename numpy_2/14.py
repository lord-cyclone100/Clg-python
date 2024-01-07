import numpy as np

# Example NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Percentiles
percentiles = [25, 50, 75]

# Calculate percentile scores
percentile_scores = np.percentile(arr, percentiles)

# Print the result
for i in range(len(percentiles)):
    print(f"{percentiles[i]}th Percentile: {percentile_scores[i]}")
