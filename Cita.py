class cita:
    def __init__ (self, idCita, patientUser, date, hour, motive, state):
        self.idCita = idCita
        self.patientUser = patientUser
        self.date = date
        self.hour = hour
        self.motive = motive
        self.state = state
        self.doctor = ""

    def getId(self):
        return self.idCita

    def getHour(self):
        return self.hour
    
    def getPatientUser(self):
        return self.patientUser
    
    def getDate(self):
        return self.date

    def getMotive(self):
        return self.motive

    def getState(self):
        return self.state

    def getDoctor(self):
        return self.doctor

    def setPatientUser(self, patientUser):
        self.patientUser = patientUser

    def setDate(self, date):
        self.date = date

    def setMotive(self, motive):
        self.motive = motive

    def setState(self, state):
        self.state = state

    def setDoctor(self, doctor):
        self.doctor = doctor
        
        