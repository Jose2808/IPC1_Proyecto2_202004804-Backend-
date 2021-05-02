class Medicamento:

    def __init__ (self, idMedicamento, nombre, precio, descripcion, cantidad):
        self.idMedicamento = idMedicamento
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad
    
    def getId(self):
        return self.idMedicamento

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getDescripcion(self):
        return self.descripcion
    
    def getCantidad(self):
        return self.cantidad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrecio(self, precio):
        self.precio = precio

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setCantidad(self, cantidad):
        self.cantidad = cantidad