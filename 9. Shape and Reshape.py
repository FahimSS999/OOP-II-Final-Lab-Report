import numpy as np
sensor_data = np.arange(1, 13)
try:
    reshaped = sensor_data.reshape(3, 4)
    print("Reshaped Array:\n", reshaped)
except ValueError:
    print("Reshape not possible. Adjusting the array...")
if sensor_data.size % 4 != 0:
    padded = np.pad(sensor_data,(0, 4 - sensor_data.size % 4), mode='constant')
reshaped = padded.reshape(-1, 4)
print("Padded and Reshaped Array:\n", reshaped)
