class receta:
    def __init__ (self, idReceta, date, patientUser, padecimiento, descripcion):
        self.idReceta = idReceta
        self.date = date
        self.patientUser = patientUser
        self.padecimiento = padecimiento
        self.descripcion = descripcion

    def getId(self):
        return self.idReceta

    def getHour(self):
        return self.date
    
    def getPatientUser(self):
        return self.patientUser
    
    def getPadecimiento(self):
        return self.padecimiento

    def getDescripcion(self):
        return self.descripcion

        
        