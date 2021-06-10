from matplotlib import pyplot as plt
import numpy as np

"""How to Select a Meaningful Visualization
Chart categories:

Composition charts
Focusing Question: What are the parts of some whole? What is the data made of?
Datasets that work well: Data pertaining to probabilities, proportions, and percentages can be visualized as with the graphs in this composition category. 
Charts in this category illustrate the different data components and their percentages as part of a whole.
- Pie Charts, stacking bar Charts, Stcking line charts

Distribution Charts
Datasets that work well: Data in large quantities and/or with an array of attributes works well for these types of charts. Visualizations in this 
category will allow you to see patterns, re-occurrences, and a clustering of data points.
Note: In statistics, a commonly seen distribution is a bell curve, also known as a normal distribution. 
A bell curve is a bell-shaped distribution where most of the values in the dataset crowd around the average (also known as the mean), 
therefore causing the curve to form. If you want to see how values in the data are “distributed” across variables, the best way to do that 
would be with the visualizations in this category.
- Histograms, for few variables maybe bar charts with seperate bars (s. Two bars in one diagram)

Relationship Charts
Focusing Question: How do variables relate to each other?
Datasets that work well: Data with two or more variables can be displayed in these charts. These charts typically illustrate 
a correlation between two or more variables. You can communicate this relationship by mapping multiple variables in the same chart. 
Correlation measures the strength of a relationship between variables.
- Mostly line charts, maybe bars, for a lot of items maybe even histograms->Distribution

Comparison Charts
Focusing Question: How do variables compare to each other?
Datasets that work well: Data must have multiple variables, and the visualizations in this category allow readers to compare those items against the others. 
For example, a line graph that has multiple lines, each belonging to a different variable. Multi-colored bar charts are also a great way to compare items in data.
- Scatter plots

"""
"""Single Bar with error"""
past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
plt.figure(figsize=(10, 8))
plt.bar(range(len(years)), past_years_averages, yerr=error, capsize=5)
plt.axis([-0.5, 6.5, 70, 95])
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)

plt.title("Final Exam Averages")
plt.xlabel("Year")
plt.ylabel("Test average")
# plt.savefig("my_bar_chart.png")
plt.show()

"""Sida-by-Side Bars"""

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]


def create_x(t, w, n, d):
    return [t * x + w * n for x in range(d)]


school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)
middle_x = [school_b_x[i] - 0.4 for i in range(5)]

plt.figure(figsize=(10, 8))
ax = plt.subplot()
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)
plt.legend(["Middle School A", "Middle School B"])
plt.title("Test Averages on Different Units")
plt.xlabel("Unit")
plt.ylabel("Test Average")
plt.axis([0, 10.5, 70, 95])
# plt.savefig("my_side_by_side.png")
plt.show()

"""Stacked Bars"""
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
d_bottom = np.add(Cs, c_bottom)
f_bottom = np.add(Ds, d_bottom)
plt.figure(figsize=(10, 8))
plt.bar(x, As)
plt.bar(x, Bs, bottom=As)
plt.bar(x, Cs, bottom=c_bottom)
plt.bar(x, Ds, bottom=d_bottom)
plt.bar(x, Fs, bottom=f_bottom)
ax = plt.subplot()
ax.set_xticks(x)
ax.set_xticklabels(unit_topics, rotation=30)
plt.title("Grade distribution")
plt.ylabel("Number of Students")
plt.xlabel("Unit")
plt.savefig("my_stacked_bar.png")
plt.show()

exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75,
                70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48, 78.81, 79.23, 74.38, 79.27, 81.07, 75.42,
                90.35, 82.93, 86.74, 81.33, 95.1, 86.57, 83.66, 85.58, 81.87, 92.14, 72.15, 91.64, 74.21, 89.04, 76.54,
                81.9, 96.5, 80.05, 74.77, 72.26, 73.23, 92.6, 66.22, 70.09, 77.2]

plt.figure(figsize=(10, 8))
plt.hist(exam_scores1, bins=12, normed=True, histtype='step', linewidth=2)
plt.hist(exam_scores2, bins=12, normed=True, histtype='step', linewidth=2)
plt.legend(["1st Yr Teaching", "2nd Yr Teaching"])
plt.title("Final Exam Score Distribution")
plt.xlabel("Percentage")
plt.ylabel("Frequency")
# plt.savefig("my_histogram.png")
plt.show()
