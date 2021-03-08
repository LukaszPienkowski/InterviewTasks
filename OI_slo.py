import csv
import numpy as np
import pandas as pd

## Zmiana danych do pliku csv i arrayów dla lepszej analizy
with open('slo3.in', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(" ") for line in stripped if line)
    with open('slo3.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
        
df = pd.read_csv('slo3.csv', sep = '\s+', header = None)
numpy_df = df.to_numpy()
n, w, a, b = numpy_df[0,0], numpy_df[1,0], numpy_df[2,0], numpy_df[3,0] #Wyciągnięcie wierszy z wspólnego pliku
n_s, w_s, a_s, b_s = n.split(','), w.split(','), a.split(','), b.split(',') #Rozbicie danych co ','

#Konstrukcja permutacji p
p = {}
for i in range(0, int(n)):
    p[int(b_s[i])] = int(a_s[i])

#Rozkład p na cykle proste
odw = np.empty((1 ,int(n)), dtype=str)
for i in range(0, int(n)):
    odw[0, i] = False

C, c = {}, 0
for i in range(0, int(n)):
    if odw[0, i] == 'F':
        c = c + 1
        x = i + 1 
        while odw[0, x-1] == 'F':
            odw[0, x-1] = True
            C.setdefault(c, [])
            C[c].append(x)      
            x = p[x]

#Stworzenie cykli, które zamiast numerów słoni będą miały przypisane masy tych słoni
masa = {}
for i in range(1, int(n)+1):
    masa[i] = int(w_s[i-1])

C1, o = {}, 0
for i in range(1, len(C)+1):
    x1, x2 = C[i], len(C[i])
    o = o +1
    for j in range(0, x2):
        x3 = int(masa[x1[j]])
        C1.setdefault(o, [])
        C1[i].append(x3)

#Obliczanie wyniku
wynik = 0
for i in range(1, c+1):
    metoda1 = int(sum(C1[i])) + int((abs(len(C1[i])) - 2)) * int(min(C1[i]))
    metoda2 = int(sum(C1[i])) + int(min(C1[i])) + int(abs(len(C1[i])+1)) * int(min(w_s))
    wynik = wynik + min(metoda1, metoda2)
print(wynik)


