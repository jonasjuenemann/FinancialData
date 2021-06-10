from matplotlib import pyplot as plt
import numpy as np

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(drinks, sales1)
plt.show()
# alt:
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks, rotation=30)
plt.close('all')

"""Two bars in one diagram"""

# so nicht:
# plt.bar(drinks, sales1)
# plt.bar(drinks, sales2)
# plt.show()

n = 1  # This is our first dataset (out of 2)
t = 2  # Number of datasets
d = len(drinks)  # Number of sets of bars
w = 0.8  # Width of each bar (standard:0.8)
store1_x = [t * element + w * n for element
            in range(d)]  # [0.8, 2.8, 4.8, 6.8, 8.8, 10.8]
# store1_x = range(0,12,2)
# print(store1_x)

plt.bar(store1_x, sales1)

n = 2
store2_x = [t * element + w * n for element
            in range(d)]  # [1.6, 3.6, 5.6, 7.6, 9.6, 11.6]
# print(store2_x)
# store2_x = range(1,13,2)

plt.bar(store2_x, sales2)

ax = plt.subplot()
ax.set_xticks([store2_x[i] - 0.4 for i in range(d)])
ax.set_xticklabels(drinks, rotation=30)

plt.show()

#bars "gestapelt"
plt.bar(drinks, sales1)
plt.bar(drinks, sales2, bottom=sales1)

plt.show()

# error on bar charts
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# man koennte auch yerr=4 fuer eine konstanten error von +-4 an allen bars angeben
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error,capsize=5)

plt.show()

# error on line graphs
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
y_lower = [i*0.9 for i in revenue]
y_upper = [i*1.1 for i in revenue]

plt.plot(month_names, revenue)
plt.fill_between(month_names, y_lower, y_upper, alpha=0.2)
plt.show()

# Pie-Charts
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

# plt.pie(payment_method_freqs)
# plt.axis('equal') wenn wir betrachtung auf den Pie "von oben" wuenschen
# Fuer Labeling 2 Methoden:
# plt.legend(payment_method_names) -> sehr simpel
# besser:
# plt.pie(payment_method_freqs, labels = payment_method_names)
# for adding percentage of slices:
# autopct = '%d%%' fuer Integer mit Prozentzeichen,
# '%0.1f%%', fuer eine DezimalStelle mit Prozentzeichen,
# '%0.2f', zwei Dezimalstellen, ohne Prozentzeichen
plt.pie(payment_method_freqs, labels = payment_method_names, autopct='%0.1f%%')
plt.show()

"""Histogram:
A histogram tells us how many values in a dataset fall between different sets of numbers (i.e., how many numbers fall between 0 and 10? 
Between 10 and 20? Between 20 and 30?). Each of these questions represents a bin, for instance, our first bin might be between 0 and 10.
"""

# plt.hist finds the minimum and the maximum values in your dataset and creates 10 equally-spaced bins between those values.
# plt.hist(dataset)
# plt.show()

# If we want more than 10 bins, we can use the keyword bins to set how many bins we want to divide the data into.
# The keyword range selects the minimum and maximum values to plot
# plt.hist(dataset, range=(66,69), bins=40)

a = np.random.normal(loc=64, scale=2, size=10000)
b = np.random.normal(loc=70, scale=2, size=10000)
# For better visibility, we could:
plt.hist(a, range=(55, 75), bins=20)
plt.hist(b, range=(55, 75), bins=20)
plt.show()
# 1. Add opacity: plt.hist(a, range=(55, 75), bins=20, opacity=0.5)
# 2. histtype with the argument 'step' to draw just the outline of a histogram
plt.hist(a, range=(55, 75), bins=20, histtype='step')
plt.hist(b, range=(55, 75), bins=20, histtype='step')
plt.show()
# If one is much bigger than the other, like:
b = np.random.normal(loc=70, scale=2, size=100000)
# then we can norm them:
# plt.hist(a, range=(55, 75), bins=20, alpha=0.5, normed=True)
# plt.hist(b, range=(55, 75), bins=20, alpha=0.5, normed=True)
# funktioniert aus irgendwelchen Gruenden nicht.

"""Pie Chart"""
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

plt.figure(figsize=(10,8))
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%d%%')
plt.axis('equal')
plt.title("Hardest Topics")
plt.savefig("my_pie_chart.png")
plt.show()

"""Line with error"""
hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]

# Create your figure here
plt.figure(figsize=(10,8))
plt.plot(exam_scores, hours_reported, linewidth=2)
# Create your hours_lower_bound and hours_upper_bound lists here
hours_lower_bound = [i*0.8 for i in hours_reported]
hours_upper_bound = [i*1.2 for i in hours_reported]
# Make your graph here
plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha=0.2)
plt.title("Time spent studying vs final exam scores")
plt.xlabel("Score")
plt.ylabel("Hours studying (self-reported)")
plt.savefig("my_line_graph.png")
plt.show()