class cine:
    def __init__(self):
        self.funciones = {}
        self.ventas =[]
        self.contador = 1

def crear_funcion(self, hora, precio):
    id_funcion = self.contador 
    self.funciones[id_funcion]= {'hora': hora, 'precio': precio,'vendidos': 0}
    self.contador += 1
    print (f"funcion (id_funcion) creada - {hora}- ${precio}")
    
    def listar_funciones(self):
        print
        time.sleep (2)
        for id_funcion, datos in
        self.funciones.items ():
        print(f"{id_funcion}:{datos['hora']} - ${datos['precio']}")

        def vender_boletos (self, id_funcion, cantidad):
            if id_funcion not in 
            self.funciones: 
            print("X funcion no existe")

            return 
        if cantidad <= 0:
            print ("X cantidad invalida")
            return 
        precio = self.funciones [id_funcion]['precio']
        total = precio * cantidad 

        self.ventas.append ({'id : id_funcion, 'cantidad': cantidad, ´total': tottal})
        self.funciones [id_funcion]
        ['vendidos'] += cantidad
