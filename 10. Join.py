import numpy as np
a1 = np.array([100, 200, 300])
a2 = np.array([150, 250, 350])
horizontal = np.column_stack((a1, a2))
print("Horizontal Join:\n", horizontal)
vertical = np.vstack((a1, a2))
print("Vertical Join:\n", vertical)
