"""1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo 
para un rango de números indicado por un usuario."""

numeros=[]

for i in range (1,21):
    numeros.append(i)

print (numeros)


"""2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por 
ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50"""

numero_ingresado=int(input("ingrese un numero"))
numero_lista=[]
for i in range (1,11):
    operacion= i*numero_ingresado    
    numero_lista.append(operacion)

print (numero_lista)


"""3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir caracteres."""

lista=[]

cadena=input ("ingrese unas palapras:")

for i in cadena:
    if (i not in lista):
        lista.append(i)

print (lista)



"""4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios."""

lista=[]

cadena=input ("ingrese unas palapras:")

for i in cadena:
    if(i != " "):
        lista.append(i)

print (lista)


"""5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se 
repite."""

import random
lista = []
contador = 0
for i in range(100):
    lista.append (random.randint(0,100))

tupla = tuple (lista)

numero_solicitado = int (input ("ingrese un numero del 0 al 100 para ver cuantas veces se repite en la tupla: "))

for i in tupla:
    if numero_solicitado == i:
        contador += 1

print ("El ", numero_solicitado, "se repitió:", contador, "veces")


"""6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta 
entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino 
muestra un mensaje de error. El programa termina cuando el usuario introduce un 
cero"""

tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

numero_ingresado = int(input("Ingrese un numero del 1 al 12, PERO RECUERDE: Si ingresa el 0 éste programe se terminará"))

while True:
        if numero_ingresado == 0:
            break
        elif numero_ingresado >= 1 and numero_ingresado <=12:
            print (tupla [numero_ingresado-1])  
            numero_ingresado = int(input("Ingrese un numero del 1 al 12, PERO RECUERDE: Si ingresa el 0 éste programe se terminará"))
        
        elif numero_ingresado > 12:
            print ("El numero ingresado no corrsponde. Ingrese un numero válido")
            numero_ingresado = int(input("Ingrese un numero del 1 al 12, PERO RECUERDE: Si ingresa el 0 éste programe se terminará"))
        
        elif numero_ingresado < 0:
            print ("El numero ingresado no corrsponde. Ingrese un numero válido")
            numero_ingresado = int(input("Ingrese un numero del 1 al 12, PERO RECUERDE: Si ingresa el 0 éste programe se terminará"))

"""7) Crea una tupla con números e indica el número con mayor valor y el que menor 
tenga."""
import random
lista = []

for i in range(100):
    lista.append (random.randint(-100,100))

tupla = tuple (lista)
minimo = (0)
maximo = (0)

for i in tupla:
    if i > maximo:
        maximo = i
    if i < minimo:
        minimo = i

print ("El máximo número en la tupla es:", maximo)
print ("El mínimo número en la tupla es:", minimo)


"""8) (Opcional)Escribir un programa que vaya solicitando al usuario que ingrese 
nombres. - Si el nombre se encuentra en la agenda (implementada con un 
diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no 
es correcto. - Si el nombre no se encuentra, debe permitir ingresar el teléfono 
correspondiente. El usuario puede utilizar la cadena "*", para salir del programa"""


"""9) Opcional: Pide números y mételos en una lista, cuando el usuario meta un 0 ya 
dejaremos de insertar. Por último, muestra los números ordenados de menor a 
mayor."""

lista = []
numeros = int(input("Ingrese un numero"))

while True:
    if numeros !=0:
        lista.append (numeros)
        numeros = int(input("Ingrese un numero"))
    elif numeros == 0:
        break

lista.sort()
print (lista)


"""10) Opcional: Lo mismo que el anterior, pero ordenando de mayor a menor"""

lista = []
numeros = int(input("Ingrese un numero"))

while True:
    if numeros !=0:
        lista.append (numeros)
        numeros = int(input("Ingrese un numero"))
    elif numeros == 0:
        break

lista.sort()
lista = lista [::-1]

print (lista)