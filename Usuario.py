class usuarioPaciente:
    def __init__ (self, idPaciente, name, last_name, birth, sex, user_name, password, phone):
        self.idPaciente = idPaciente
        self.name = name
        self.last_name = last_name
        self.birth = birth
        self.sex = sex
        self.user_name = user_name
        self.password = password
        self.phone = phone
        self.citas = []
        self.type = 1

    def agregarCita(self, cita):
        self.citas.append(cita)

    def getId(self):
        return self.idPaciente

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def getLast_name(self):
        return self.last_name
    
    def getBirth(self):
        return self.birth

    def getSex(self):
        return self.sex

    def getUser_name(self):
        return self.user_name

    def getPassword(self):
        return self.password

    def getPhone(self):
        return self.phone

    def setId(self, idPaciente):
        self.idPaciente = idPaciente

    def setName(self, name):
        self.name = name

    def setLast_name(self, last_name):
        self.last_name = last_name

    def setBirth(self, birth):
        self.birth = birth

    def setSex(self, sex):
        self.sex = sex

    def setUser_name(self, user_name):
        self.user_name = user_name

    def setPassword(self, password):
        self.password = password

    def setPhone(self, phone):
        self.phone = phone

    def setType(self, type):
        self.type = type

class usuarioEnfermera:

    def __init__ (self, idEnfermera, name, last_name, birth, sex, user_name, password, phone):
        self.idEnfermera = idEnfermera
        self.name = name
        self.last_name = last_name
        self.birth = birth
        self.sex = sex
        self.user_name = user_name
        self.password = password
        self.phone = phone
        self.type = 2

    def getId(self):
        return self.idEnfermera

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def getLast_name(self):
        return self.last_name
    
    def getBirth(self):
        return self.birth

    def getSex(self):
        return self.sex

    def getUser_name(self):
        return self.user_name

    def getPassword(self):
        return self.password

    def getPhone(self):
        return self.phone

    def setName(self, name):
        self.name = name

    def setId(self, idEnfermera):
        self.idEnfermera = idEnfermera

    def setLast_name(self, last_name):
        self.last_name = last_name

    def setBirth(self, birth):
        self.birth = birth

    def setSex(self, sex):
        self.sex = sex

    def setUser_name(self, user_name):
        self.user_name = user_name

    def setPassword(self, password):
        self.password = password

    def setPhone(self, phone):
        self.phone = phone

    def setType(self, type):
        self.type = type

class usuarioMedico:

    def __init__ (self, idMedico, name, last_name, birth, sex, user_name, password, phone):
        self.idMedico = idMedico
        self.name = name
        self.last_name = last_name
        self.birth = birth
        self.sex = sex
        self.user_name = user_name
        self.password = password
        self.phone = phone
        self.citasAsignadas = 0
        self.type = 3

    def getId(self):
        return self.idMedico

    def getCitas(self):
        return self.citasAsignadas

    def getSpeciality(self):
        return self.speciality

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def getLast_name(self):
        return self.last_name
    
    def getBirth(self):
        return self.birth

    def getSex(self):
        return self.sex

    def getUser_name(self):
        return self.user_name

    def getPassword(self):
        return self.password

    def getPhone(self):
        return self.phone
    
    def setId(self, idMedico):
        self.idMedico = idMedico

    def setCitasAsignadas(self, citasAsignadas):
        self.citasAsignadas = citasAsignadas

    def setName(self, name):
        self.name = name

    def setLast_name(self, last_name):
        self.last_name = last_name

    def setBirth(self, birth):
        self.birth = birth

    def setSex(self, sex):
        self.sex = sex

    def setUser_name(self, user_name):
        self.user_name = user_name

    def setPassword(self, password):
        self.password = password

    def setPhone(self, phone):
        self.phone = phone

    def setType(self, type):
        self.type = type

    def setSpeciality(self, speciality):
        self.speciality = speciality
