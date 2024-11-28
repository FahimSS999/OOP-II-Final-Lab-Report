import numpy as np
prices = np.array([15, 20, 25, 30, 50, 60])
filtered_prices = prices[(prices >= 20) & (prices <= 50)]
print("Filtered Prices:", filtered_prices)