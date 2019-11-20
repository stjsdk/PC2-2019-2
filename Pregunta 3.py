import os,sys
os.system("cls")

i = 0
a = 5
hombres = 0
mujeres = 0
nombres = []
sexos = []
edades = []
sum_edades = 0
prom_edades = 0
print("----Inscripciones para natación----")
while (i<a):
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)

    sexo = input("Ingrese su sexo (H/M): ")   
    while True :
        if sexo.lower() == "h":
            hombres = hombres + 1
            sexos.append("hombre")
            break
        if sexo.lower() == "m":
            mujeres = mujeres + 1
            sexos.append("mujer")
            break
        else:
            sexo = input("Ingrese su sexo correctamente (H/M): ")


    edad = int(input("Ingrese su edad: "))
    while True :
        if edad>=5 and edad<18:
            edades.append(edad)
            print("---------")
            break
        else:
            edad = int(input("Ingrese una edad válida: "))
        

    
    i = i + 1

print("----Lista de inscritos----")
print(" ")
for i in range(0,a):
    print(" ")
    print("Inscrito #",i+1)
    print(" ")
    print("Nombre: ",nombres[i])
    print("Sexo = ", sexos[i])
    print("Edad = ",edades[i])
    sum_edades = sum_edades + edades[i]
prom_edades = sum_edades*0.2
print(" ")
print("Cantidad de hombres = ", hombres)
print("Cantidad de mujeres = ", mujeres)
print("Promedio de edades = ", prom_edades)