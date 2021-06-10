import numpy as np

# mean auf 2D Array

allergy_trials = np.array([[6, 1, 3, 8, 2],
                           [2, 6, 3, 9, 8],
                           [5, 2, 6, 9, 9]])

total_mean = np.mean(allergy_trials)
print(total_mean)
trial_mean = np.mean(allergy_trials, axis=1)
print(trial_mean)
patient_mean = np.mean(allergy_trials, axis=0)
print(patient_mean)

temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

sorted_temps = np.sort(temps, )
print(sorted_temps)
# für desc order
sorted_temps = -np.sort(-temps)
print(sorted_temps)

median_temps = np.median(temps, )
print(median_temps)