from io import StringIO

import pandas as pd


def Test(string):
    if (string == "s"):
        print("s")
        return
    print("not s")


print([a * b for a, b in zip([2, 3, 4], [3, 4, 5])])

df = pd.DataFrame([
    ['January', 100, 100, 23, 100],
    ['February', 51, 45, 145, 45],
    ['March', 81, 96, 65, 96],
    ['April', 80, 80, 54, 180],
    ['May', 51, 54, 54, 154],
    ['June', 112, 109, 79, 129]],
    columns=['month', 'clinic_east',
             'clinic_north', 'clinic_south',
             'clinic_west'])

print(df.index)
print("hier")
print(
    [list(i[1]) for i in df.loc[1:3].iterrows()])  # ohne list() wäre i[1] hier eine Pandas.Series (=> df mit 1 column)
# df into 2D Array
values = df.values
print(values)

# Adding rows:
df.loc[666] = ['July', 100, 91, 82, 99]  # adding a row, muss auf einem unbelegten index sein
df.index = df.index + 1  # shifting index (anstatt von 0-666, 1-667)
df = df.sort_index()  # sorting by index

print(df)

# funktioniert nicht:
df2 = pd.DataFrame([['August', 100, 91, 82, 99]], columns=['month', 'clinic_east',
                                                           'clinic_north', 'clinic_south',
                                                           'clinic_west'])

df = df.append(df2,
               ignore_index=True)  # ignore_index=True, sonst gibt er der neuen Reihe den niedrigsten unbelegten index (hier: 0). So "resettet" er die indexes auf 0-7

print(df)

# adding a column and a row with the sum totals

df.loc['Column_Total'] = df.sum(numeric_only=True, axis=0)
df.loc[:, 'Row_Total'] = df.sum(numeric_only=True, axis=1)

print(df)

# MultiIndexing

import numpy as np

a = pd.read_csv(StringIO('T,Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz,Dx,Dy,Dz\n\
    0,1,2,1,3,2,1,4,2,1,5,2,1\n\
    1,8,2,3,3,2,9,9,1,3,4,9,1\n\
    2,4,5,7,7,7,1,8,3,6,9,2,3'))
a.set_index('T', inplace=True)

a.columns = pd.MultiIndex.from_tuples([(c[0], c[1]) for c in a.columns])

print(a)

original_str = 'abcdefghijklmnopqrstuvwxyz'
print(original_str[-2:0:-1])
# a[start:stop:step] -> bei -1 step -> umgekehrte Reihenfolge, start -2: fängt beim vorletzten Element an. geht bis zum ersten Argument(0), schließt dieses aber noch aus.
