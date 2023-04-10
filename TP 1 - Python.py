"""1. Mensaje simple: Almacene un mensaje en una variable e imprímalo en pantalla. 
Después cambie el valor del mensaje e imprímalo nuevamente."""

mensaje= "TP1 IITA"
print(mensaje)
mensaje= "TP1 IITA Nuevo"
print(mensaje)

"""2. Almacene el nombre de una persona en una variable, imprima un mensaje para esa persona. 
Por ejemplo “Hola Fede, ¿te gustaría aprender a programar?”"""

nombre= input("Coloque su nombre")
print(f"Hola {nombre}, ¿te gustaría aprender a programar?")

"""3. El número ocho: Escriba una suma, resta, multiplicación y división que resulten cada una en el número ocho. 
Asegúrese de utilizar la función print() para ver los resultados en pantalla. 
Un ejemplo de línea es el siguiente:
print(5 + 3)
La salida debería mostrar el número ocho tantas veces como líneas haya escrito."""

suma=1+1+1+1+1+1+1+1
resta=100-92
multiplicacion=8*1
division= int(88/11)
print(suma)
print(resta)
print(multiplicacion)
print(division)

"""4. Cree cuatro variables llamadas mi_entero, mi_decimal, mi_string y mi_booleano. 
Asigne a cada variable un valor del tipo que le corresponda. 
Luego muestre en pantalla el tipo de cada variable usando la función type() combinando todo con la función print() : 
type(mi_entero) type(mi_booleano)
La salida final debería contener las siguientes líneas (no importa el orden): 
<class 'int'> <class 'float'> <class 'str'> <class 'bool'>"""

mi_entero= 5
mi_decimal= 0.5
mi_string= "cinco"
mi_booleano= True
print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_string))
print(type(mi_booleano))

"""5. Escriba un programa que acepte un numero decimal como entrada y lo imprima sin lugares decimales."""

numero_ingreado=float (input("ingrese un numero (que no sea entero)"))
print(int(numero_ingreado))

"""6. ¿Cuál es la salida de las siguientes expresiones? 
1 != 2
Salida: 
True == 1
Salida: 
False != False
Salida: 
False > 0
Salida: 
1.0 < 1
Salida: 
“test” == “test”
Salida: 
1.0 >= 1
Salida:"""

variable_1=1 != 2
salida_1= bool(variable_1)
print(salida_1)
variable_2=True == 1
salida_2= bool(variable_2)
print(salida_2)
variable_3=False != False
salida_3= bool(variable_3)
print(salida_3)
variable_4=False > 0
salida_4= bool(variable_4)
print(salida_4)
variable_5=1.0 < 1
salida_5= bool(variable_5)
print(salida_5)
variable_6="test" == "test"
salida_6= bool(variable_6)
print(salida_6)
variable_7=1.0 >= 1
salida_7= bool(variable_7)
print(salida_7)

"""7. (Opcional) Escriba un programa que le pida al usuario que ingrese nombre y edad. 
Luego muestre un mensaje donde le informe el año en que va a cumplir 100."""

nombre=input("ingrese su nombre")
edad=int(input("ingrese su edad"))
operacion=((2023-edad+100))
print(f"Hola {nombre}, sabías que en el año {operacion} vas a cumplir los 100 años?")

"""8. (Opcional) Escriba un programa que permita convertir una temperatura en Celsius a la escala Farenheit. 
La fórmula es: Fahrenheit = (9.0/5.0) x Celsius + 32"""

temperatura_C= float(input("Ingrese la temperatura (en Celcius)"))
operacion=((9.0/5.0) * temperatura_C + 32)
print(f"La temperatura ingresada equivale a {operacion} grados Farenheit")

"""9. (Opcional) Calculadora simple: Cree un programa capaz de pedir dos números al usuario y devolver 
el resultado de la suma, resta, multiplicación y división entre los mismos. 
Por ejemplo, si los números son 3 y 5, la calculadora nos devolvería: 3+5; 3-5; 3*5 y 3/5. 
Pruebe también expandir su calculadora y agregar nuevas operaciones, tales como la potenciación o la división entera."""

primer_numero=float(input("ingrese un numero"))
segundo_numero=float(input("ingrese otro numero"))
suma= primer_numero + segundo_numero
resta= primer_numero - segundo_numero
multiplicacion= primer_numero * segundo_numero
division= primer_numero / segundo_numero
potencia= primer_numero ** segundo_numero
division_entera= primer_numero // segundo_numero
print (f"la suma del primer numero con el segundo numero es:{suma}")
print (f"la resta del primer numero con el segundo numero es:{resta}")
print (f"la multiplicacion del primer numero con el segundo numero es:{multiplicacion}")
print (f"la division del primer numero con el segundo numero es:{division}")
print (f"la potencia del primer numero con el segundo numero es:{potencia}")
print (f"la division entera del primer numero con el segundo numero es:{division_entera}")