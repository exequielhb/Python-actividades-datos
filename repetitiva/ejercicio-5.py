pregunta = int(input("ingresa un numero: "))


while pregunta != 0:
    if pregunta % 2 == 0:
        print("tu numero es par ", pregunta)
    elif pregunta % 1 == 0:
        print("tu numero es impar")
    pregunta = int(input("ingresa un numero: "))
if pregunta == 0:
    print("Terminaste")