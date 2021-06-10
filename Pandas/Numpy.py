import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.genfromtxt('../data/data_sample.csv', delimiter=',')
test_3 = np.array([87, 85, 72, 90, 92])
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

print(np.array(student_scores[2, 0]))

# elementwise operations
l = [1, 2, 3, 4, 5]
a = np.array(l)
a_plus_3 = a + 3
print(a_plus_3)
# elementwise operations mit mehreren arrays
test_3_fixed = test_3 + 2
total_grade = test_1 + test_2 + test_3_fixed
final_grade = total_grade / 3
print(final_grade)

# 2D Arrays, wichtig: Reihen muessen selbe anzahl an Elementen haben.
coin_toss = np.array([1, 0, 0, 1, 0])
coin_toss_again = np.array([[1, 0, 0, 1, 0],
                            [0, 0, 1, 1, 1]])
# indexing in 2D array in numpy -> little different
tanya_test_3 = student_scores[2, 0]
cody_test_scores = np.array(student_scores[:, -1])  # fuer ganze columns

# logical operators:
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
# print(porridge > 70) #[ True False False False False  True  True  True  True False]
cold = porridge[porridge < 60]
hot = porridge[porridge >= 80]
just_right = porridge[(porridge >= 60) & (porridge <= 80)]  # | fuer oder
print(cold, hot, just_right)

temperatures = np.genfromtxt('../data/data_temperature.csv', delimiter=',')
print(temperatures)
temperatures_fixed = temperatures + 3
monday_temperatures = temperatures_fixed[0]
thursday_friday_morning = temperatures_fixed[-2:, 1]
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
