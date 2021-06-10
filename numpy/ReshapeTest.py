import numpy as np

list = np.array(list(range(12)))
print(list)

list = list.reshape(-1, 1) # erzeugt x Reihen mit einem Wert (1 Column)
#(1,-1) erzeugt eine Reihe mit x Werten
print(list)

list = list.reshape(12)
print(list)

# list = list.reshape(5, -1) funktioniert nicht, (cannot reshape array of size 12 into shape (5,newaxis))