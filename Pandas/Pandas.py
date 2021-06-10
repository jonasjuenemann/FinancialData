import pandas as pd

df1 = pd.DataFrame({
    'Product ID': [1, 2, 3, 4],
    # add Product Name and Color here
})

#df = pd.read_csv('../data/data_imdb.csv') #csv einlesen
#print(df.head())
#print(df.info())

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

january = df["month"] == "January"
#print(january)
january = df[df["month"] == "January"]
#print(january)
march_april = df[(df["month"] == "March") | (df["month"] == "April")]
#print(march_april)

january_february_march = df[df.month.isin(['January',
     'February',
     'March',"October"])] #nimmt Oktober nicht wahr, sucht trotzdem alle anderen

print(january_february_march)
print()
df2 = df.loc[[1, 3, 5]]
#print(df2)
df3 = df2.reset_index()
df2.reset_index(inplace=True, drop=True) #inplace -> bekannt, drop -> sorgt dafuer, dass der alte index keine neue spalte wird
#print(df2)
#print(df3)


"""shoetype"""
orders = pd.read_csv("../data/data_shoefly.csv")
#print(orders.head())
emails = orders["email"]
frances_palmer = orders.loc[(orders["first_name"] == "Frances")] #.loc[] ist hier nicht noetig, ist aber die bessere practice
print(frances_palmer)
comfy_shoes = orders[(orders["shoe_type"] == "clogs") | (orders["shoe_type"] == "boots") | (orders["shoe_type"] == "ballet flats")]
# alt. comfy_shoes = orders[(orders["shoe_type"].isin(["clogs", "boots", "ballet flats"])]
print(comfy_shoes)

# Adding Columns
""""""
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'Hammer', 3.00, 5.50],
  [4, 'Screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
# df['Sold in Bulk?'] = ["Yes", "Yes", "No", "No"] -> offensichtlich
df['Is taxed?'] = 'Yes'  # Yes fuer alle Spalten
df['Margin'] = df.Price - df["Cost to Manufacture"]
# df["Lowercase Description"] = df["Description"].apply(lambda x: x.lower()), oder:
df["Lowercase Description"] = df["Description"].str.lower()


"""Anwendung von apply auf Zeilen, abhaengig von den Werten in bestimmten Zeilen"""
df['Price with Tax'] = df.apply(lambda row:
     row['Price'] * 1.075
     if row['Is taxed?'] == 'Yes'
     else row['Price'],
     axis=1
)
print(df)
#lambda Funktionen
mylambda = lambda x: x[0] + x[-1]
secondlambda = lambda x: "Welcome to BattleCity!" if 13 <= x < 69 else "You must be over 13" if x < 13 else "Nice one Boomer" #mult. if-conditions
"""employees"""
employees = pd.read_csv('../data/data_employees.csv')
#print(df)
get_last_name = lambda x: x.split(" ")[-1] #wuerde von vollem Namen, Nachnamen abtrennen (wenn per whitespace getrennt)
employees["last_name"] = employees["name"].apply(get_last_name)
total_earned = lambda x: x["hourly_wage"]*x["hours_worked"]+0.5*x["hourly_wage"]*(x["hours_worked"]-40) if x["hours_worked"] > 40 else x["hourly_wage"]*x["hours_worked"]
employees["total_earned"] = employees.apply(total_earned,axis=1) #axis=1 fuer die Reihenweise Anwendung
print(employees)
#df.columns = ["ID","Name","Wage/h","WorkHours"] aendert die Column Namen

""""""
orders.rename(columns={
    'first_name': 'FirstName'},
    inplace=True) #zu praeferieren, da: man braucht nicht unbedingt alle ZeilenNamen zu aendern und es nicht weiter dramatisch ist sich zu verschreiben
orders = orders.rename(columns={
    'shoe_type': 'Type'})
orders["shoe_source"] = orders["shoe_material"].apply(lambda x: "vegan" if x not in ["leather"] else "animal")
orders["salutation"] = orders.apply(lambda x: "Dear Mr. " + x["last_name"] if x["gender"] == "male" else "Dear Ms. " + x["last_name"], axis=1)
print(orders)