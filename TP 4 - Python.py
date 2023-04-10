"""1)Escriba una función que muestre todos los números primos 
entre 1 y un número n que es ingresado por parámetro."""
# def primos(x):
    
#     for numero in range (x, 3, -1):
        
#         for divisor in range (2, numero):

#             operacion1 = numero % divisor
#             operacion2 = numero / divisor

#             if operacion1 != 0 and operacion2 == 1:
#                 print (numero, end= " ")

# x = int (input())
# primos (x)


# def primos(x):
#     for i in range (2, x+1):
#         divisor = 2

#         while i % divisor != 0:
#             divisor +=1
#             if divisor == i:
#                 print (i, end= " ")

# numero= int(input("Ingrese un numero positivo y entero"))
# x = numero
# primos (x)



"""2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, 
hasta que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje 
avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del programa de acuerdo 
a estos criterios:
• Use un test condicional en el ciclo while para detener la ejecución.
• Use un test condicional dentro del ciclo para decidir si continuar la ejecución."""

# condimento = input("Ingrese un condimento: ")

# clave = "salir"

# while True:
#     if condimento != clave:
#         condimento = input("Ingrese otro condimento: ")
#     else:
#         break
       

"""otra solucion:"""

# condimento = input("Ingrese un condimento: ")

# while condimento != "salir":
#     condimento = input("Ingrese otro condimento: ")
#     if condimento == "salir":
#         break


"""3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un tamaño y el mensaje 
que debería ir impreso en la remera. La función debe mostrar un mensaje describiendo el tamaño de la remera y 
el mensaje impreso en ella. Llame la función una vez usando argumentos por posición. Llámela una segunda vez 
usando argumentos por clave.
B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por defecto sea ‘L’ y el mensaje,
 ‘Me gusta Python’. Haga un par de remeras, la primera con los valores por defecto, y la segunda con valores 
 diferentes."""
def hacer_remera (tamaño, mensaje):
    tamaño = input("ingrese el tamaño de la remera que desea")
    mensaje = input("ingrese el mensaje que desea imprimir")


    
remeras = {"s":"Remera talle S","m":"Remera talle M", "l":"Remera talle L", "xl":"Remera talle XL", "xxl":"Remera talle XXL"}



"""4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros 
de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo número 
es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …)."""


# def fibonacci(x):
#     n_antepenultimo = 0
#     n_penultimo = 1
#     n_ultimo = 0
#     for i in range (numero_D_veces):
   
#         n_ultimo = n_penultimo + n_antepenultimo
        
#         n_antepenultimo = n_penultimo
#         n_penultimo = n_ultimo
#         print (n_ultimo, end= " ")

# numero_D_veces = int(input("ingrese el numero de la serie de Fibonacci que quiere conocer: "))
# x = numero_D_veces
# fibonacci (numero_D_veces)

"""5) (Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que 
la calculadora sea capaz de devolver el resultado solamente de una operación especificada por el usuario. 
Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la calculadora devuelve la suma 
entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc."""

# primer_numero = float(input("ingrese un numero"))
# segundo_numero = float(input("ingrese otro numero"))

# operacion_elegida = input("Ingrese el numero que representa la operación que quiere realizar, siendo estos: 1 para suma; 2 para resta; 3 para multiplicacion; 4 para division; 5 para potencia o 6 para division entera")

# if operacion_elegida != "1" or "2" or "3" or "4" or "5" or "6":
#     operacion_elegida = input("Has elegido una opcion incorrecta, ingresa nuevamente la operacion que deseas realizar, siendo: 1 para suma; 2 para resta; 3 para multiplicacion; 4 para division; 5 para potencia o 6 para division entera")

# operaciones = {
# "1": primer_numero + segundo_numero,
# "2": primer_numero - segundo_numero,
# "3": primer_numero * segundo_numero,
# "4": primer_numero / segundo_numero,
# "5": primer_numero ** segundo_numero,
# "6": primer_numero // segundo_numero}

# print("El resultado de la operacion elegida es:", operaciones [operacion_elegida])


"""6) (Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir gramos a libras, 
centímetros a pulgadas y kilómetros a millas. 
El programa debe permitir la conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 
pulgadas = 1 cm 0.00220462 libras = 1 gramo"""

# numero = float(input("Ingrese el numero que quiera convertir: "))
# operacion_elegida = input("Elige la operación que prefieras, ingresando: kilometro_a_milla o milla_a_kilometro o centimetro_a_pulgada o pulgada_a_centimetro o gramo_a_libra o libra_a_gramo")
# if operacion_elegida != "kilometro_a_milla" or "milla_a_kilometro" or "centimetro_a_pulgada" or "pulgada_a_centimetro" or "gramo_a_libra" or "libra_a_gramo":
#     operacion_elegida = input("Has escrito incorrectamente la operación elegida, vuelve a intentarlo, elige entre las siguientes operaciones: kilometro_a_milla o milla_a_kilometro o centimetro_a_pulgada o pulgada_a_centimetro o gramo_a_libra o libra_a_gramo")
# operaciones = {
# "kilometro_a_milla" : numero * 1.60934,
# "milla_a_kilometro" : numero / 1.60934,
# "centimetro_a_pulgada" : numero * 0.393701,
# "pulgada_a_centimetro" : numero / 0.393701,
# "gramo_a_libra" : numero * 0.00220462,
# "libra_a_gramo" : numero / 0.00220462}

# print(numero, "convertido de ", operacion_elegida, "es:", operaciones [operacion_elegida])

"""7) (Opcional) Cuando un año es bisiesto, el mes más corto del año, febrero, tiene 29 días en vez de 28. 
Esto sucede casi cada 4 años. 
Los tres criterios que permiten saber si un año es bisiesto en el calendario gregoriano (el nuestro) 
son los siguientes:
• Si el año es divisible enteramente por 4, es bisiesto a menos que: 
o El año sea divisible por 100, entonces NO es bisiesto, a menos que:
▪ El año sea también divisible por 400. Entonces sí es un año bisiesto. 
Esto significa que en el calendario gregoriano los años 2000 y 2400 son bisiestos, 
mientras que los años 1900, 2100, 2200 y 2300 no son bisiestos.
a) Escriba una función que tome un año y diga si es bisiesto o no.
b) Modifique su programa para que devuelva todos los años bisiestos entre el año actual 
y el año pasado a la función como parámetro (este debe ser posterior al año actual)."""

# año = int(input("Ingrese el año que desea comprobar: "))

# if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
#     print ("El año ", año, "ES BISIESTO")
# else:
#     print ("El año ", año, "NO ES BISIESTO")

# año = int(input("Ingrese el año que desea comprobar: (recuerde que tiene que ser un año posterior al año actual)"))
# años_biciestos = []
# for i in range (2023, año+1):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#         años_biciestos.append(i)

# print ("Los años bisiestos que vendran entre el año actual y el ingresado serán: ", años_biciestos)


"""8) (Opcional) Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5, 
obtenemos 3,5,6 y 9. La suma de estos múltiplos es 23. 
Encuentre la suma de todos los múltiplos de 3 o 5 menores a 1000."""

# numero = int(input("rango de valor"))
# suma = 0
# for i in range (1, numero):

#     if i % 3 == 0 or i % 5 == 0:
#         suma += i

# print (suma)