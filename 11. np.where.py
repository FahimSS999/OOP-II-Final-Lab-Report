import numpy as np
temperatures = np.array([30, 22, 35, 18, 40, 25])
high_temp_indices = np.where(temperatures > 30)
print("High Temperature Indices:", high_temp_indices)
modified_temps = np.where(temperatures < 25, 25, temperatures)
print("Modified Temperatures:", modified_temps)