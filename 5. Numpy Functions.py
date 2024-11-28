import numpy as np
scores = np.array([[85, 90, 78], [88, 76, 92], [70,
80, 85]])
averages = np.mean(scores, axis=1)
print("Averages:", averages)
best_student = np.argmax(averages)
print(f"Student {best_student + 1} has the highest average: {averages[best_student]}")