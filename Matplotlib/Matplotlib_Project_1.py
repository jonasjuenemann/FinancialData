from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

# Spezifische Aufgabe (von mir fuer mich: einmaliges Setzen der labels fuer beide subplots, etwas komplizierter)
# create your figure here
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot() # großer plot um beide drumherum
ax.set_xlabel("Months")
ax.set_ylabel("Visits")
# geht nicht, da Figure noch keine labels hat (erst ein plot dann)
# fig.set_xlabel("Months")
# fig.set_ylabel("Visits")
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)
# ausblenden der Achsen etc. des "großen subplots

"""
Alternativ:
fig.text(0.5, 0.04, 'common xlabel', ha='center', va='center')
fig.text(0.06, 0.5, 'common ylabel', ha='center', va='center', rotation='vertical')
zum setzen von labels manuell
"""

ax1 = fig.add_subplot(1, 2, 1)
x_values = range(len(months))
ax1.plot(x_values, visits_per_month, marker="o")
# waeren die einzelnen labels
#ax1.set_xlabel("Months")
#ax1.set_ylabel("Visits")
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
ax1.set_title(" Visits per Month")

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x_values, key_limes_per_month)
ax2.plot(x_values, persian_limes_per_month)
ax2.plot(x_values, blood_limes_per_month)
#ax2.set_xlabel("Months")
#ax2.set_ylabel("Visits")
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
ax2.legend(["Key Limes", "Persian Limes", "Blood Times"])
ax2.set_title("Lime Sales")

plt.subplots_adjust(wspace=0.25, bottom=0.1, top=0.9, right=0.9, left=0.1)
plt.savefig("test.jpg")

plt.show()
