""" Realizá un programa que permita registrar cantidad de 
colillas recolectadas por un número determinado de personas. 
Luego obtener estadísticas al respecto informando porcentaje de 
personas que han encontrado menos de 100 colillas, 
más de 100 y menos de 200, más de 200 colillas. """


personas = 0
menosdecien = 0
masymenosdoscientos = 0
masdoscientos = 0

contador = 1

while contador > 0:
    colillas = int(input("cuantas colillas recolecto? "))
    personas += 1

    if colillas < 100:
        menosdecien +=1
    elif colillas > 100 and colillas < 200:
        masymenosdoscientos +=1
    elif colillas > 200:
        masdoscientos +=1
    break

porcentaje_menoscien = (menosdecien/personas) * 100
pocentaje_masymenosdoscientos = (masymenosdoscientos/personas) * 100
pocentaje_masdoscientos = (masdoscientos/personas) * 100

print("encontraron menos de 100 colillas", porcentaje_menoscien)
print("encontraron entre 100 y 200 colillas", pocentaje_masymenosdoscientos)
print("encontraron mas de 100 colillas", pocentaje_masdoscientos)