vehiculos = 0
cont_basura = 0
cont_multa = 0

continuar = "si"

while continuar == "si":
    valor_cadena = input("ingrese valor de monitoreo para avanzar: ")
    vehiculos += 1

    if valor_cadena[-1] == "1":
        cont_multa += 1
    
    if valor_cadena[-2] == "1":
        cont_basura += 1
    
    continuar = input("desea seguir ingresando datos para analizar? si/no").lower()

porc_multados = (cont_multa/ vehiculos) * 100

print("cantidad de vehiculos analizados: ", vehiculos)
print("cantidad de vehiculos que tiraron basura: ", cont_basura)
print("cantidad de vehiculos multados: ", porc_multados.__round__())
