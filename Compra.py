class compra:

    def __init__ (self, idMedicamento, nombre, cantidadComprada):
        self.idMedicamento = idMedicamento
        self.nombre = nombre
        self.cantidadComprada = cantidadComprada
    
    def getId(self):
        return self.idMedicamento

    def getNombre(self):
        return self.nombre
    
    def getCantidad(self):
        return self.cantidadComprada

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCantidad(self, cantidadComprada):
        self.cantidadComprada = cantidadComprada