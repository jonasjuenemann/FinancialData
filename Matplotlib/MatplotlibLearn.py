from matplotlib import pyplot as plt

days = [0,1,2,3,4,5,6]
money_spent = [10, 12, 12,10,14,22, 24]
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]

plt.plot(days, money_spent)
plt.plot(days, money_spent_2)
#plt.show()
plt.close('all')

"""
# Dashed:
plt.plot(x_values, y_values, linestyle='--')
# Dotted:
plt.plot(x_values, y_values, linestyle=':')
# No line:
plt.plot(x_values, y_values, linestyle='')

#Farben
plt.plot(days, money_spent, color='green')
plt.plot(days, money_spent_2, color='#AAAAAA')

# marker -> Line gibt es durchaus noch, aber an den Punkten marker
# A circle:
plt.plot(x_values, y_values, marker='o')
# A square:
plt.plot(x_values, y_values, marker='s')
# A star:
plt.plot(x_values, y_values, marker='*')
"""

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue, color='purple', linestyle="--")
plt.plot(time, costs, color="#82edc9", marker="s")
plt.show()
plt.close('all')


x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
"""
plt.axis([0, 3, 2, 5])
The minimum x-value displayed x=0
The maximum x-value displayed x=3
The minimum y-value displayed y=2
The maximum y-value displayed y=5
"""
# gibt lediglich kleinen Ausschnitt des Graphen wieder
plt.axis([0, 3, 2, 5])
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')
#plt.show()
plt.close('all')

"""Subplots

The command plt.subplot() needs three arguments to be passed into it:

The number of rows of subplots
The number of columns of subplots
The index of the subplot we want to create
"""
# Data sets
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

# First Subplot
plt.subplot(1, 2, 1)  # 1 row of subplots with 2 columns, First Subplot
plt.plot(months, temperature)
plt.title('First Subplot')

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(months, flights_to_hawaii)
plt.title('Second Subplot')

# Display both subplots
plt.show()

"""
We can customize the spacing between our subplots to make sure that the figure we create is visible and easy to understand. To do this, we use the 
plt.subplots_adjust() command. .subplots_adjust() has some keyword arguments that can move your plots within the figure:

left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label
right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, or decrease it to make room for a legend
bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an x-axis label
top — the top margin, with a default of 0.9
wspace — the horizontal space between adjacent subplots, with a default of 0.2
hspace — the vertical space between adjacent subplots, with a default of 0.2
"""

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

# Man beachte: der obere Plot soll die komplette Breite ausfuellen (daher hier eine column)
# Top Plot
plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

# In der zweiten Reihe sollen zwei Plots stehen, daher: column 2, da der erste Subplot soz. Plaetze 1 und 2 belegt -> bei 3 weiter
# Left Plot
plt.subplot(2, 2, 3)
plt.plot(x, parabola)

# Right Plot
plt.subplot(2, 2, 4)
plt.plot(x, cubic)

# Subplot Adjust
plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()

# Legende
"""
plt.legend() can also take a keyword argument loc, which will position the legend on the figure.

These are the position values loc accepts:
0	best
1	upper right
2	upper left
3	lower left
4	lower right
5	right
6	center left
7	center right
8	lower center
9	upper center
10	center
"""
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue, color='purple', linestyle="--")
plt.plot(time, costs, color="#82edc9", marker="s")
plt.legend(['revenue', 'Costs'], loc=4)
#plt.show()

"""Modify Ticks"""
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

ax = plt.subplot()
ax.set_xticks(months)  # ax.set_yticks()
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])  # ax.set_yticks()
ax.set_yticklabels(["10%", "25%", "50%", "75%"])

#plt.show()

# fuer den Fall, dass wir noch vergessene plt.plot() lines haben, die nicht geshowed wurden, koennen wir benutzen:
plt.close('all')

"""figures
We can use the command plt.figure() to create new figures and size them how we want. We can add the keyword figsize=(width, height) 
to set the size of the figure, in inches. We use parentheses (( and )) to pass in the width and height, which are separated by a comma (,).

To create a figure with a width of 4 inches, and height of 10 inches, we would use:
plt.figure(figsize=(4, 10))

After plotting, we can call plt.savefig('name_of_graph.png')
"""

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')
plt.close("all")
plt.figure(figsize=(7, 3)) #width, height -> muss vor dem plot definiert werden
plt.plot(years, power_generated)
plt.savefig('power_generated.png')
#plt.show()

plt.close("all")