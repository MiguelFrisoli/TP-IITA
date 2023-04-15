class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.r_nombre = restaurante_nombre
        self.t_comida = tipo_comida

    def __str__(self) -> str:
        self.r_nombre
        self.t_comida
        return
    
    def describir_Restaurante (self):
        print (self.r_nombre)
        print (self.t_comida)
        return

    def abrir_restaurante (self):
        print (self.r_nombre," Está abierto")
        return
    
class Heladeria(Restaurante):
    def __init__ (self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.s_helados = sabores
    
    def describir_Heladeria (self):
        print (self.r_nombre)
        print (self.t_comida)
        print (self.s_helados)
        return