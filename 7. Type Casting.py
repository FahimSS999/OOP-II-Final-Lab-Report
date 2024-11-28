import numpy as np
data = np.array([['21', 'Fahim', '50000.50'],
['22', 'Sakib', '60000.75']])
ages = data[:, 0].astype(int)
print("Ages:", ages)
salaries = data[:, 2].astype(float)
print("Salaries:", salaries)
