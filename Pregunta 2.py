import os,sys
os.system("cls")

palabra = []
parametro = []

i = 0
a = input("Ingrese una palabra ")
b = input("Ingrese un parámetro ")
 
for x in range(0,len(a)):
    if b in a:
        i = i +1

print(i)
