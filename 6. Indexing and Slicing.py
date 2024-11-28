import numpy as np
sales_data = np.array([[100, 200, 300, 400],
 [150, 250, 350, 450],
 [200, 300, 400, 500],
 [250, 350, 450, 550]])
print("First 3 products:\n", sales_data[:3])
print("Last 2 months:\n", sales_data[:, -2:])
print("2nd product in 4th month:",
sales_data[1, 3])
