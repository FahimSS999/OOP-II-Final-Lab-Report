import numpy as np
data = np.array([[10, 20, 30], [40, 50, 60], [70,
80, 90]])
x = data[0].view()
y = data[:, 0].copy()
print("View of row:", x)
print("Copy of column:", y)
x[1] = 60
y[1] = 100
print("Updated data array:")
print(data)