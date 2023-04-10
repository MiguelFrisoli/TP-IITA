# 1 Pida un número al usuario y determine si es par o impar"""

numero= int(input("ingrese un numero"))
if numero % 2 == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")

# 2) Escriba una cadena if-elif-else que determine el estado de vida de una persona.
"""• Si la persona tiene menos de 2 años, muestre un mensaje que diga que es un bebe.
• Si tiene al menos 2 años, pero menos de 4, muestre que es un infante.
• Si tiene al menos 4, pero menos de 12, muestre que es un niño.
• Si tiene al menos 13, pero menos de 20, muestre que es un adolescente.
• Si tiene al menos 20 pero menos de 65, muestre que es un adulto.
• Si tiene 65 o más, muestre que es un anciano."""

edad=int(input("ingrese la edad"))
if edad >64:
    print("Anciano")
elif edad > 19 and edad < 65:
    print("Adulto")
elif edad > 12 and edad < 20:
    print("Adolecente")
elif edad > 3 and edad < 13:
    print("Niño")
elif edad > 1 and edad < 4:
    print("Infante")
else:
    print("Bebé")

# 3) Cree un ciclo que nunca termine y ejecútelo. 
"""Puede probarlo haciendo que muestre algo en pantalla por cada pasada del ciclo. 
Para finalizarlo, presione Ctrl-C o el comando para detener la ejecución correspondiente a su editor"""

variable=10
while variable > 0:
    print(variable)

# 4) Escriba un programa que contenga dos ciclos while anidados que muestre los enteros del 1 al 100, 
"""diez números por línea, como se muestra abajo:
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
. . 91 92 93 94 95 96 97 98 99 100"""

variable=0
for variable in range (1,101,10):
    print(variable,variable+1,variable+2,variable+3,variable+4,variable+5,variable+6,variable+7,variable+8,variable+9)

# 5) Resuelva el ejercicio anterior usando solo un ciclo while

variable=1
while variable<101:
    print(variable,variable+1,variable+2,variable+3,variable+4,variable+5,variable+6,variable+7,variable+8,variable+9)
    variable+=10


