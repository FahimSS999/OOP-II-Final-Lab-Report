import numpy as np
scores = np.array([50, 75, 90, 65, 85])
indices_75 = np.where(scores == 75)
indices_90 = np.where(scores == 90)
print("Indices of 75:", indices_75)
print("Indices of 90:", indices_90)
ascending = np.sort(scores)
descending = np.sort(scores)[::-1]
print("Ascending:", ascending)
print("Descending:", descending)