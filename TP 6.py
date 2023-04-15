"""1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y 
que contenga un método que devuelva el área del rectángulo."""

# class Rectangulo:
#     base : float
#     altura : float

#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def Area (self):
#         return self.base * self.altura
        

# base = int(input("ingrese le valor de la base"))
# altura = int(input("ingrese el valor de la altura"))
# rectangulo1 = Rectangulo (base, altura)
# print("El área del rectangulo es igual a:",rectangulo1.Area(),"centimetros cuadrados")

"""2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. 
La clase debe contener como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, 
se debe lanzar una excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, 
se debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. 
En ese caso la cantidad de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir 
un mensaje de aviso: “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""

# class Mate:


#     def __init__(self,c_Cebadas, volumen, c_m_Cebada):
#         self.c_Cebada = c_Cebadas
#         self.volumen = volumen
#         self.c_m_Cebada = c_m_Cebada

#     def Cebar (self):
#         if self.volumen > 10:
#             print ("te quemaste")
#         elif self.volumen > 9:
#             print ("Ojo, el mate está lleno")
#             pregunta = input("querés cebar igual")
#             if  pregunta == "SI":
#                 self.volumen += 5
#                 self.c_Cebada += 1
#                 self.c_m_Cebada -= 1
#         else:
#             self.volumen < 1
#             print("el mate está vacío, cebalo")
#             pregunta = input("querés cebarlo?")
#             if  pregunta == "SI":
#                 self.volumen += 5
#                 self.c_Cebada += 1
#                 self.c_m_Cebada -= 1
#             else:
#                 print("Si no lo cebas, no vas a poder tomar mate")
#         return
        

#     def Tomar (self):
#         if self.c_m_Cebada > 1 and self.volumen > 0:
#             print("la yerba está lavada")
#             pregunta = input("querés tomar?")
#             if pregunta != "SI":
#                 pregunta = input("te vuelvo a preguntar, querés tomar?")
#             elif pregunta == "SI":    
#                 self.volumen -= 5
#                 print("Puaj, el mate está lavado")
#         elif self.volumen <1:
#             print ("El mate está vacío, cebalo")
#         return
     

# mate1 = Mate(0, 0, 10)
# mate1.Cebar()
# mate1.Cebar()
# mate1.Tomar()


"""3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, 
o None si está destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y 
se guarde una referencia al corcho sacado. 
Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que 
no haya un corcho."""

# class Corcho:
#     def __init__(self, Bodega):
#         self.Bodega=Bodega
    
#     def __str__(self):
#         return self.Bodega

# class Botella:
#     def __init__(self, Corcho:Corcho):
#         self.CorchoDeBotella=Corcho

# class Sacacorcho:
#     def __init__(self):
#         self.CorchoSacacorcho=None
    
#     def Descorchar(self,Botella:Botella):
#         if self.CorchoSacacorcho==None:
#             if Botella.CorchoDeBotella!=None:
#                 self.CorchoSacacorcho=Botella.CorchoDeBotella
#                 Botella.CorchoDeBotella=None
#                 print("Botella descorchada")
#             else:
#                 print("La botella ya esta descorchada")
#         else:
#             print("El sacacorchos ya tiene un corcho, primero limpialo")
            
#     def Limpiar(self):
#         if self.CorchoSacacorcho==None:
#             print("El sacacorchos ya esta limpio")
#         else:
#             self.CorchoSacacorcho=None
#             print("El sacacorcho está limpio")

# bodega = Corcho ("D.V. Catena")
# botella = Botella (bodega)


"""4) Una heladería es un tipo especial de restaurante. 
Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: restaurante_nombre y tipo_comida. 
Cree un método describir_restaurante() que muestre estas piezas de información, y un método abrir_restaurante() 
que muestre un mensaje indicando que el restaurante ahora está abierto. 
Luego cree una clase Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores 
que almacene una lista de los sabores de helado disponibles. 
Escriba también un método que muestre estos valores, cree una instancia de la clase y llame al método."""

# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.r_nombre = restaurante_nombre
#         self.t_comida = tipo_comida

#     def __str__(self) -> str:
#         self.r_nombre
#         self.t_comida
#         return
    
#     def describir_Restaurante (self):
#         print (self.r_nombre)
#         print (self.t_comida)
#         return

#     def abrir_restaurante (self):
#         print (self.r_nombre," Está abierto")
#         return
    
# class Heladeria(Restaurante):
#     def __init__ (self, restaurante_nombre, tipo_comida, sabores):
#         super().__init__(restaurante_nombre, tipo_comida)
#         self.s_helados = sabores
    
#     def describir_Heladeria (self):
#         print (self.r_nombre)
#         print (self.t_comida)
#         print (self.s_helados)
#         return


# restaurante_1 = Restaurante ("La Monumental", ["parrilla", "pastas", "minutas"])
# heladeria_1 = Heladeria ("Fili", "Helados", ["limon", "maracuya", "sambayon"])

# restaurante_1.describir_Restaurante()
# restaurante_1.abrir_restaurante()
# heladeria_1.describir_Heladeria()
# heladeria_1.abrir_restaurante()




"""5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, 
y los métodos recibir_ataque, que reduzca la vida según una cantidad recibida y 
lance una excepción si la vida pasa a ser menor o igual que cero, y mover que reciba una dirección y 
se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, 
que reciba otro personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, 
que devuelva la cantidad cosechada"""

# class Personaje:
#     def __init__(self, vida, posicion, velocidad):
#         self.Vida = vida
#         self.Posicion = posicion
#         self.Velocidad = velocidad
    
#     def recibir_ataque (self):
#         self.Vida -= 1
#         if self.Vida <= 0:
#             print ("Eres comida para gusanos!")
#         return
    
#     def mover (self):
#         self.Posicion = input("elegir avanzar o retroceder")
#         if self.Posicion == "avanzar":
#             self.Posicion += 1 * self.Velocidad
#         if self.Posicion == "retroceder":
#             self.Posicion -= 1 * self.Velocidad
#         return

# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad, ataque):
#         super(). __init__(vida, posicion, velocidad)
#         self.Ataque = ataque

#     def atacar (self):
#         self.Vida -= self.Ataque


# class Campesino(Personaje):
#     def __init__(self, vida, posicion, velocidad, cosechar):
#         super().__init__(vida, posicion, velocidad)
#         self.Cosechar = cosechar

#     def cosechar (self):
#         self.Cosechar *= self.Velocidad
#         print("el campesino cosechó:", str(self.Cosechar*self.Velocidad), "unidades")
#         return
    


"""6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos 
que típicamente se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen 
de la información del usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno."""

# class Usuario:
#     def __init__(self, nombre, apellido, mail, dni):
#         self.Nombre = nombre
#         self.Apellido = apellido
#         self. Mail = mail
#         self.Dni = dni
    
#     def __str__(self) -> str:
#         self.Nombre
#         self.Apellido
#         self. Mail
#         self.Dni
#         return
    
#     def describir_Usuario(self):
#         return print(self.Nombre, self.Apellido, self. Mail, self.Dni)
    
#     def saludar_Usuario(self):
#         return print("Hola", self.Nombre, self.Apellido, "bienvenido!")

# usuario1 = Usuario ("Juan", "Perez", "JP@Hotmail.com", "123123")
# usuario2 = Usuario ("Pedro", "Sanchez", "PS@hotmail.com", "456456")
# usuario3 = Usuario ("Luis", "Gonzales", "LG@hotmail.com", "789789")

# usuario1.describir_Usuario()
# usuario2.describir_Usuario()
# usuario3.describir_Usuario()

# usuario3.saludar_Usuario()
# usuario2.saludar_Usuario()
# usuario1.saludar_Usuario()


"""7) Admin: Un administrador es un tipo de usuario con privilegios especiales. 
Cree una clase Admin que herede de la clase Usuario del ejercicio anterior y agréguele un atributo privilegios 
que almacene una lista de strings tales como “puede postear en el foro”, “puede borrar un post”, 
“puede banear usuario”, etc. 
Escriba un método mostrar_privilegios() que muestre el conjunto de privilegios del administrador, 
cree una instancia de la clase y llame al método."""

# class Usuario:
#     def __init__(self, nombre, apellido, mail, dni):
#         self.Nombre = nombre
#         self.Apellido = apellido
#         self. Mail = mail
#         self.Dni = dni
    
#     def __str__(self) -> str:
#         self.Nombre
#         self.Apellido
#         self. Mail
#         self.Dni
#         return
    
#     def describir_Usuario(self):
#         return print(self.Nombre, self.Apellido, self. Mail, self.Dni)
    
#     def saludar_Usuario(self):
#         return print("Hola", self.Nombre, self.Apellido, "bienvenido!")

# class Administrador(Usuario):
#     def __init__(self, nombre, apellido, mail, dni, privilegios):
#         super().__init__(self, nombre, apellido, mail, dni,)
#         self.Privilegios = privilegios == ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]
        
    
#     def __str__(self) -> str:
#         self.Privilegios
#         return

#     def mostrar_privilegios(self):
#         return print (self.Privilegios)

# administrador1 = Administrador("Juan", "Perez", "JP@Hotmail.com", "123123", )
# administrador1.mostrar_privilegios()


"""8) Privilegios: Escriba una clase Privilegios. 
La clase debería tener un atributo, privilegios, que almacene una lista de strings con los privilegios 
de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta clase, 
y haga que una instancia de esta clase sea un atributo de la clase Admin. 
Cree una nueva instancia de Admin y use el método para mostrar privilegios."""



"""9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, 
e impórtela al módulo actual. 
Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación funcionó."""

# from ejercicio9delpractico6 import Restaurante

# restaurante_1 = Restaurante ("La Monumental", ["parrilla", "pastas", "minutas"])


# restaurante_1.describir_Restaurante()
# restaurante_1.abrir_restaurante()


"""10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. 
¿Qué se necesita para que funcione la importación?"""

# from ejercicio9delpractico6 import *


# heladeria_1 = Heladeria ("Fili", "Helados", ["limon", "maracuya", "sambayon"])

# heladeria_1.describir_Heladeria()
# heladeria_1.abrir_restaurante()