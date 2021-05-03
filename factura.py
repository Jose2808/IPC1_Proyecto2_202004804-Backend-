class factura:
    def __init__ (self, idFactura, date, patientUser, doctorUser, precioConsulta, precioOperacion, total):
        self.idFactura = idFactura
        self.date = date
        self.patientUser = patientUser
        self.doctorUser = doctorUser
        self.precioConsulta = precioConsulta
        self.precioOperacion = precioOperacion
        self.total = total

    def getId(self):
        return self.idFactura

    def getHour(self):
        return self.date
    
    def getPatientUser(self):
        return self.patientUser
    
    def getDoctorUser(self):
        return self.doctorUser

    def getPrecioConsulta(self):
        return self.precioConsulta

    def getPrecioOperacion(self):
        return self.precioOperacion

    def getTotal(self):
        return self.total