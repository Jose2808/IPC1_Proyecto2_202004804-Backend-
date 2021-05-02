from flask import Flask, jsonify, request
from flask_cors import CORS
from Medicamento import Medicamento
from Usuario import usuarioEnfermera
from Usuario import usuarioPaciente
from Usuario import usuarioMedico
from Compra import compra
from Cita import cita
from Receta import receta
import json 

usuarios = []
citas = []
medicamentos = []
medicamentosComprados = []
recetas = []

app = Flask(__name__)
CORS(app)

usuarios.append(usuarioPaciente(0, "Ariel", "Bautista", "28/08/2001", "M", "admin", "1234", 12345))
usuarios.append(usuarioMedico(1, "Juan", "Silva", "28/08/2001", "M", "Juan1234", "12345678", 12345))
usuarios[1].setSpeciality("Neurocirujano")
usuarios.append(usuarioEnfermera(2, "Sofía", "Perez", "28/08/2001", "F", "Sofi56", "12345678", 12345))
usuarios.append(usuarioEnfermera(3, "Juana", "Fernandez", "28/08/2001", "F", "JuanaArch", "12345678", 12345))
usuarios.append(usuarioMedico(4, "Pedro", "Gonzalez", "28/08/2001", "M", "Peter54", "12345678", 12345))
usuarios[4].setSpeciality("Dentista")
usuarios.append(usuarioPaciente(5, "Firulais", "Mendez", "28/08/2001", "M", "FiruFiru", "12345678", 12345))
usuarios.append(usuarioPaciente(6, "Rodrigo", "Mendez", "28/08/2001", "M", "Rodrigo59", "12345678", 12345))
usuarios[0].setType(0)
medicamentos.append(Medicamento(len(medicamentos) + 1, "Ibuprofeno", 1.00, "Para dolores corporales", 0))
medicamentos.append(Medicamento(len(medicamentos) + 1, "Acetaminofen", 2.50, "Para fiebre", 100))
medicamentos.append(Medicamento(len(medicamentos) + 1, "Yodoclorina", 3.00, "Para descontrol estomacal", 75))
medicamentos.append(Medicamento(len(medicamentos) + 1, "Vitaflenaco", 2.50, "Para dolores musculares", 80))
medicamentos.append(Medicamento(len(medicamentos) + 1, "Panadol", 1.50, "Para gripe", 125))
citas.append(cita(1,"Jose2808", "05-08-20201", "10:00", "Dolor de estómago", "Pendiente"))
citas.append(cita(2,"Juan1234", "05-08-20201", "10:00", "Dolor de garganta", "Pendiente"))
citas.append(cita(3,"Peter54", "05-08-20201", "10:00", "Dolor de espalda", "Pendiente"))
citas.append(cita(4,"FiruFiru", "05-08-20201", "10:00", "Dolor de cabeza", "Pendiente"))


@app.route('/', methods = ['GET'])
def frontPage():
    return("Bienvenido al sistema de UHospital")

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.json["user"]
        password = request.json["password"]
        for usuario in usuarios:
            if user == usuario.getUser_name():
                if password == usuario.getPassword():
                    objeto = {
                        'Mensaje':'Se ha iniciado sesión con éxito',
                        'User': usuario.getUser_name(),
                        'Tipo': usuario.getType(),
                        'Exist': True
                    }
                    break
                else:
                     objeto = {'Mensaje':'Contraseña incorrecta',
                     'Exist': False
                    }
                break     
            else:
                objeto = {
                    'Mensaje':'Usuario incorrecto',
                    'Exist': False
                }
    return(jsonify(objeto))

@app.route('/registroPaciente', methods = ['POST'])
def registrarPaciente():
    if request.method == 'POST':
        idUsuario = len(usuarios)
        name = request.json['name']
        surname = request.json['surname']
        birthDate = request.json['birth']
        sex = request.json['sex']
        username = request.json['user']
        password = request.json['password']
        phone = request.json['phone']

        if len(password) < 8:
            objeto = {'Mensaje': 'La contraseña debe ser de al menos 8 caracteres'}
        else:
            for usuario in usuarios:
                if username == usuario.getUser_name():
                    user_exist = True
                    break
                else:
                    user_exist = False

            if user_exist == True:
                objeto = {'Mensaje': 'Usuario ya existente, intente de nuevo'}
            else:    
                nuevo_usuario = usuarioPaciente(idUsuario, name, surname, birthDate, sex, username, password, phone)
                usuarios.append(nuevo_usuario)   
                objeto = {'Mensaje': 'Usuario ingresado con éxito'} 
    return jsonify(objeto)

@app.route('/carga-masiva/Pacientes', methods = ['POST'])
def cargaPacientes():
    if request.method == 'POST':
        listaPacientes = request.json['pacientes']
        for paciente in listaPacientes:
            nuevo_usuario = usuarioPaciente(len(usuarios), paciente['name'], paciente['surname'], paciente['birth'], paciente['sex'], paciente['user'], paciente['password'], paciente['phone'])
            usuarios.append(nuevo_usuario)
        objeto = {'Mensaje': 'Carga masiva con éxito'}
    return(jsonify(objeto))

@app.route('/carga-masiva/Doctores', methods = ['POST'])
def cargaDoctores():
    if request.method == 'POST':
        listaDoctores = request.json['doctores']
        for doctor in listaDoctores:
            nuevo_doctor = usuarioMedico(len(usuarios), doctor['name'], doctor['surname'], doctor['birth'], doctor['sex'], doctor['user'], doctor['password'], doctor['phone'])
            nuevo_doctor.setSpeciality(doctor['speciality'])
            usuarios.append(nuevo_doctor)
        objeto = {'Mensaje': 'Carga masiva con éxito'}
    return(jsonify(objeto))

@app.route('/carga-masiva/Enfermeras', methods = ['POST'])
def cargaEnfermeras():
    if request.method == 'POST':
        listaEnfermeras = request.json['enfermeras']
        for enfermera in listaEnfermeras:
            nueva_enfermera = usuarioEnfermera(len(usuarios), enfermera['name'], enfermera['surname'], enfermera['birth'], enfermera['sex'], enfermera['user'], enfermera['password'], enfermera['phone'])
            usuarios.append(nueva_enfermera)
        objeto = {'Mensaje': 'Carga masiva con éxito'}
    return(jsonify(objeto))

@app.route('/carga-masiva/Medicamentos', methods = ['POST'])
def cargaMedicamentos():
    if request.method == 'POST':
        listaMedicamentos = request.json['medicamentos']
        for medicamento in listaMedicamentos:
            nuevo_medicamento = Medicamento(len(medicamentos), medicamento['name'], float(medicamento['price']), medicamento['description'], int(medicamento['amount']))
            medicamentos.append(nuevo_medicamento)
        objeto = {'Mensaje': 'Carga masiva con éxito'}
    return(jsonify(objeto))              

@app.route('/Procesar-compra', methods = ['POST'])
def procesarCompra():
    if request.method == 'POST':
        listaCompra = request.json['listaCompras']
        for compras in listaCompra:
            medicamentoComprado = compras['name']
            cantidadComprada = int(compras['amount'])
            for medicamento in medicamentos:
                if medicamento.getNombre() == medicamentoComprado:
                    medicamento.setCantidad(medicamento.getCantidad() - int(cantidadComprada))
                    if medicamento.getCantidad() < 0:
                        objeto = {'Mensaje': 'No hay suficientes cantidades en existencia para su compra', 'producto': medicamento.getNombre()}
                        medicamento.setCantidad(medicamento.getCantidad()+ cantidadComprada)
                    else:
                        if len(medicamentosComprados) == 0:
                            compra_nueva = compra(medicamento.getId(), compras['name'], cantidadComprada)
                            medicamentosComprados.append(compra_nueva)
                            objeto = {'Mensaje': 'su compra fue realizada con éxito'}
                        else:
                            for compraMedicamento in medicamentosComprados:
                                if compraMedicamento.getNombre() == medicamentoComprado:
                                    product_exist = True
                                    break
                                else:
                                    product_exist = False
                                
                            if product_exist == True:
                                compraMedicamento.setCantidad(int(compraMedicamento.getCantidad()) + int(cantidadComprada))
                                objeto = {'Mensaje': 'su compra fue realizada con éxito'}
                            else:
                                compra_nueva = compra(medicamento.getId(), compras['name'], int(cantidadComprada))
                                medicamentosComprados.append(compra_nueva)
                                objeto = {'Mensaje': 'su compra fue realizada con éxito'} 
    return(jsonify(objeto))

@app.route('/Guardar/Receta', methods = ['POST'])
def guardarReceta():
    idReceta = len(recetas)
    userDoctor = request.json['idDoctor']
    fecha = request.json['date']
    paciente = request.json['patient']
    padecimiento = request.json['padecimiento'].upper()
    descripcion = request.json['descripcion']

    nueva_receta = receta(idReceta, fecha, paciente, padecimiento, descripcion)
    recetas.append(nueva_receta)

    for user in usuarios:
        if userDoctor == user.getUser_name():
            user.setCitasAsignadas(user.getCitas() + 1)
            doctor_exist = True
            objeto = {'Mensaje':'Cita agregada con éxito', 'Doctor': user.getUser_name(), 'Citas': user.getCitas()}
            break
        else:
            doctor_exist = False
    if doctor_exist == False:
        objeto = {'No se encontró su usuario en el sistema'}  
    return(jsonify(objeto))

@app.route('/Usuario/Crear-cita', methods = ['POST'])
def crearCita():
    if request.method == 'POST':
        idCita = len(citas)+1
        user = request.json['user']
        date = request.json['date']
        hour = request.json['hour']
        motive = request.json['motive']
        state = "Pendiente"
        if len(citas) == 0:
            nueva_cita = cita(idCita, user, date, hour, motive, state)
            citas.append(nueva_cita)
            objeto = {'Mensaje' : 'La cita se ha agregado exitosamente'}
        else:
            for citaUser in citas:
                if citaUser.getPatientUser() == user and (citaUser.getState() == "Pendiente" or citaUser.getState() == "Aceptada"):
                    cita_permitida = False
                    break
                else:
                    cita_permitida = True
            if cita_permitida == True:
                nueva_cita = cita(idCita, user, date, hour, motive, state)
                citas.append(nueva_cita)
                objeto = {'Mensaje' : 'La cita se ha agregado exitosamente'}
            else:
                objeto = {'Mensaje' : 'Usted ya tiene una cita pendiente o en proceso'}

    return(jsonify(objeto))

@app.route('/lista-citas', methods=['GET'])
def rutaLista():
    Datos = []
    for cita in citas:
        objeto = {'user':  cita.getPatientUser() , 'date': cita.getMotive()}
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/citas/pendientes', methods=['GET'])
def listasPendientes():
    Datos = []
    for cita in citas:
        if cita.getState() == "Pendiente":
            objeto = {'id': cita.getId(), 'user':  cita.getPatientUser() , 'date': cita.getDate(), 'hour': cita.getHour(), 'motive': cita.getMotive()}
            Datos.append(objeto)
        else:
            objeto = {'Mensaje': 'Usted no tiene citas pendientes'}
    return(jsonify(Datos))

@app.route('/citas/rechazadas', methods=['GET'])
def listasRechazadas():
    Datos = []
    for cita in citas:
        if cita.getState() == "Rechazada":
            objeto = {'id': cita.getId(), 'user':  cita.getPatientUser() , 'date': cita.getDate(), 'hour': cita.getHour(), 'motive': cita.getMotive()}
            Datos.append(objeto)
        else:
            objeto = {'Mensaje': 'Usted no tiene citas rechazadas'}
    return(jsonify(Datos))

@app.route('/citas/aceptadas', methods=['GET'])
def listasAceptadas():
    Datos = []
    for cita in citas:
        if cita.getState() == "Aceptada":
            objeto = {'id': cita.getId(), 'user':  cita.getPatientUser() , 'date': cita.getDate(), 'hour': cita.getHour(), 'motive': cita.getMotive()}
            Datos.append(objeto)
        else:
            objeto = {'Mensaje': 'Usted no tiene citas aceptadas'}
    return(jsonify(Datos))
            
@app.route('/cita/rechazar', methods = ['POST'])
def rechazarCita():
    idCita = request.json['id']
    for cita in citas:
        if cita.getId() == int(idCita):
            cita_exist = True
            cita.setState("Rechazada")
            objeto = {'Mensaje':'La cita ha sido rechazada con éxito'}
            break
        else:
            cita_exist = False
    if cita_exist == False:
        objeto = {'Mensaje':'No se encontró la cita a rechazar'}
    return(jsonify(objeto))

@app.route('/cita/aceptar', methods = ['POST'])
def aceptarCita():
    idCita = request.json['idCita']
    userDoctor = request.json['user']
    for cita in citas:
        if cita.getId() == int(idCita):
            cita_exist = True
            cita.setState("Aceptada")
            cita.setDoctor(userDoctor)
            objeto = {'Mensaje': 'La cita ha sido aceptada', 'idCita': cita.getId(), 'Doctor': cita.getDoctor()}
            break
        else:
            cita_exist = False
        if cita_exist == False:
            objeto = {'Mensaje':'No se encontró la cita'}
    return(jsonify(objeto))

@app.route('/Doctor/MisCitas/<string:username>', methods = ['GET'])
def obtenerMisCitas(username):
    Datos = []
    for cita in citas:
        if cita.getDoctor() == username:
            objeto = {'id': cita.getId(), 'user':  cita.getPatientUser() , 'date': cita.getDate(), 'hour': cita.getHour(), 'motive': cita.getMotive()}
            Datos.append(objeto)
        else:
            objeto = {'Mensaje':'Usted no tiene citas asignadas'}
    return(jsonify(Datos))
            
@app.route('/Medicamentos', methods = ['GET'])
def obtenerMedicinas():
    Datos = []
    for medicamento in medicamentos:
        if medicamento.getCantidad() > 0:
            objeto = { 'id': medicamento.getId(), 'name': medicamento.getNombre(), 'price': medicamento.getPrecio(), 'description': medicamento.getDescripcion(), 'amount': medicamento.getCantidad()}
            Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/registroCompras', methods = ['GET'])
def obtenerCompras():
    Datos = []
    for compras in medicamentosComprados:
        objeto = { 'id': compras.getId(), 'name': compras.getNombre(), 'amount': compras.getCantidad()}
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Medicamentos/<string:medicina>', methods = ['GET'])
def obtenerMedicina(medicina):
    if request.method == 'GET':
        for medicamento in medicamentos:
            if medicamento.getNombre() == medicina:
                objeto = {'name': medicamento.getNombre(), 'price': medicamento.getPrecio(), 'description': medicamento.getDescripcion(), 'cantidad': medicamento.getCantidad()}
                break
            else:
                objeto = {'Mensaje': 'Este producto no se encuentra disponible'}
    return(jsonify(objeto))

@app.route('/Usuario/<string:username>', methods = ['GET'])
def ObtenerUsuario(username):
    if request.method == 'GET':
        for name in usuarios:
            if username == name.getUser_name():   
                objeto = {
                    'name': name.getName(),
                    'surname': name.getLast_name(),
                    'birth': name.getBirth(),
                    'sex': name.getSex(),
                    'user': name.getUser_name(),
                    'password': name.getPassword(),
                    'phone': name.getPhone()
                }
                break
            else:
                objeto = {
                    'mensaje': 'Este usuario no existe'
                }
    return (jsonify(objeto))

@app.route('/Usuario/citas/<string:username>', methods = ['GET'])
def obtenerCitasUsuario(username):
    citasUsuario = []
    if request.method == 'GET':
        for cita in citas:
            if cita.getPatientUser() == username:
                objeto = {'hour': cita.getHour(), 'date': cita.getDate(), 'motive': cita.getMotive(), 'estado': cita.getState()}
                citasUsuario.append(objeto)
        return(jsonify(citasUsuario))           

@app.route('/Doctor/<string:username>', methods = ['GET'])
def ObtenerDoctor(username):
    if request.method == 'GET':
        for name in usuarios:
            if username == name.getUser_name():   
                objeto = {
                    'name': name.getName(),
                    'surname': name.getLast_name(),
                    'speciality': name.getSpeciality(),
                    'birth': name.getBirth(),
                    'sex': name.getSex(),
                    'user': name.getUser_name(),
                    'password': name.getPassword(),
                    'phone': name.getPhone()
                }
                break
            else:
                objeto = {
                    'mensaje': 'Este usuario no existe'
                }
    return (jsonify(objeto))

@app.route('/registroMedico', methods = ['POST'])
def registrarProfesor():
    if request.method == 'POST':
        idUsuario = len(usuarios)
        name = request.json['name']
        surname = request.json['surname']
        birthDate = request.json['birth']
        sex = request.json['sex']
        speciality = request.json['speciality']
        username = request.json['user']
        password = request.json['password']
        phone = request.json['phone']

        if len(password) < 8:
            objeto = {'Mensaje': 'La contraseña debe ser de al menos 8 caracteres'}
        else:
            for usuario in usuarios:
                if username == usuario.getUser_name():
                    user_exist = True
                    break
                else:
                    user_exist = False

            if user_exist == True:
                objeto = {'Mensaje': 'Usuario ya existente, intente de nuevo'}
            else:    
                nuevo_usuario = usuarioMedico(idUsuario, name, surname, birthDate, sex, username, password, phone)
                nuevo_usuario.setSpeciality(speciality)
                usuarios.append(nuevo_usuario)   
                objeto = {'Mensaje': 'Usuario ingresado con éxito'} 
    return jsonify(objeto)

@app.route('/registroEnfermera', methods = ['POST'])
def registrarEnfermera():
    if request.method == 'POST':
        idUsuario = len(usuarios)
        name = request.json['name']
        surname = request.json['surname']
        birthDate = request.json['birth']
        sex = request.json['sex']
        username = request.json['user']
        password = request.json['password']
        phone = request.json['phone']

        if len(password) < 8:
            objeto = {'Mensaje': 'La contraseña debe ser de al menos 8 caracteres'}
        else:
            for usuario in usuarios:
                if username == usuario.getUser_name():
                    user_exist = True
                    break
                else:
                    user_exist = False

            if user_exist == True:
                objeto = {'Mensaje': 'Usuario ya existente, intente de nuevo'}
            else:    
                nuevo_usuario = usuarioEnfermera(idUsuario, name, surname, birthDate, sex, username, password, phone)
                usuarios.append(nuevo_usuario)   
                objeto = {'Mensaje': 'Usuario ingresado con éxito'} 
    return jsonify(objeto)

@app.route('/modificar-perfil', methods = ['POST'])
def modificarPerfil():
    if request.method == 'POST':
        name = request.json['name']
        surname = request.json['surname']
        birthDate = request.json['birth']
        sex = request.json['sex']
        username = request.json['user']
        new_username = request.json['newUser']
        password = request.json['password']
        phone = request.json['phone']

        if username ==  new_username:
            for user1 in usuarios:
                if new_username == user1.getUser_name():
                    if len(password) < 8:
                        objeto = {'Mensaje': 'La contraseña debe tener al menos 8 caracteres'}
                    else:
                        user1.setName(name)
                        user1.setBirth(birthDate)
                        user1.setSex(sex)
                        user1.setPassword(password)
                        user1.setPhone(phone)
                        user1.setLast_name(surname)
                        objeto = {'Mensaje': 'Datos actualizados con éxito', 'user': user1.getUser_name(), 'status': 'OK'}
        else:
            for usuario in usuarios:
                if new_username == usuario.getUser_name():
                    user_exist = True
                    break
                else:
                    user_exist = False
        
            if user_exist == True:
                objeto = {'Mensaje':'Este nombre de usuario no se encuentra disponible'}
            else:
                if len(password) < 8:
                    objeto = {'Mensaje': 'La contraseña debe de tener al menos 8 caracteres'}
                else:
                    for user in usuarios:
                        if username == user.getUser_name():
                            user.setUser_name(new_username)
                            user.setName(name)
                            user.setBirth(birthDate)
                            user.setSex(sex)
                            user.setPassword(password)
                            user.setPhone(phone)
                            user.setLast_name(surname)
                            objeto = {'Mensaje': 'Datos de usuario actualizados','user': user.getUser_name(), 'status': 'OK'}
    return jsonify(objeto)

@app.route('/modificar-perfil/Doctor', methods = ['POST'])
def modificarPerfilDoctor():
    if request.method == 'POST':
        name = request.json['name']
        surname = request.json['surname']
        birthDate = request.json['birth']
        speciality = request.json['speciality']
        sex = request.json['sex']
        username = request.json['user']
        new_username = request.json['newUser']
        password = request.json['password']
        phone = request.json['phone']

        if username ==  new_username:
            for user1 in usuarios:
                if new_username == user1.getUser_name():
                    if len(password) < 8:
                        objeto = {'Mensaje': 'La contraseña debe tener al menos 8 caracteres'}
                    else:
                        user1.setName(name)
                        user1.setBirth(birthDate)
                        user1.setSex(sex)
                        user1.setPassword(password)
                        user1.setPhone(phone)
                        user1.setLast_name(surname)
                        user1.setSpeciality(speciality)
                        objeto = {'Mensaje': 'Datos actualizados con éxito', 'user': user1.getUser_name(), 'status': 'OK'}
        else:
            for usuario in usuarios:
                if new_username == usuario.getUser_name():
                    user_exist = True
                    break
                else:
                    user_exist = False
        
            if user_exist == True:
                objeto = {'Mensaje':'Este nombre de usuario no se encuentra disponible'}
            else:
                if len(password) < 8:
                    objeto = {'Mensaje': 'La contraseña debe de tener al menos 8 caracteres'}
                else:
                    for user in usuarios:
                        if username == user.getUser_name():
                            user.setUser_name(new_username)
                            user.setName(name)
                            user.setBirth(birthDate)
                            user.setSex(sex)
                            user.setPassword(password)
                            user.setPhone(phone)
                            user.setLast_name(surname)
                            user.setSpeciality(speciality)
                            objeto = {'Mensaje': 'Datos actualizados con éxito', 'user': user.getUser_name(), 'status': 'OK'}
    return jsonify(objeto)

@app.route('/lista-usuarios', methods=['GET'])
def rutaPost():
    Datos = []
    for usuario in usuarios:
        objeto = {'id': usuario.getId(), 'nombre': usuario.getName(), 'apellido': usuario.getLast_name(), 'nacimiento': usuario.getBirth(), 'sexo': usuario.getSex(), 'user': usuario.getUser_name(), 'contraseña': usuario.getPassword(), 'telefono': usuario.getPhone()}
        Datos.append(objeto)
    return(jsonify(Datos))
    
@app.route('/lista-pacientes', methods = ['GET'])
def mostrarPacientes():
    Datos = []
    for usuario in usuarios:
        if usuario.getType() == 1:
            objeto = {'id': usuario.getId(), 'nombre': usuario.getName(), 'apellido': usuario.getLast_name(), 'nacimiento': usuario.getBirth(), 'sexo': usuario.getSex(), 'user': usuario.getUser_name(), 'contraseña': usuario.getPassword(), 'telefono': usuario.getPhone()}
            Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/lista-medicos', methods = ['GET'])
def mostrarMedicos():
    Datos = []
    for usuario in usuarios:
        if usuario.getType() == 3:
            objeto = {'id': usuario.getId(), 'nombre': usuario.getName(), 'apellido': usuario.getLast_name(), 'nacimiento': usuario.getBirth(), 'speciality': usuario.getSpeciality(), 'sexo': usuario.getSex(), 'user': usuario.getUser_name(), 'contraseña': usuario.getPassword(), 'telefono': usuario.getPhone()}
            Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/lista-enfermeras', methods = ['GET'])
def mostrarEnfermeras():
    Datos = []
    for usuario in usuarios:
        if usuario.getType() == 2:
            objeto = {'id': usuario.getId(), 'nombre': usuario.getName(), 'apellido': usuario.getLast_name(), 'nacimiento': usuario.getBirth(), 'sexo': usuario.getSex(), 'user': usuario.getUser_name(), 'contraseña': usuario.getPassword(), 'telefono': usuario.getPhone()}
            Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Medicamentos', methods = ['POST'])
def getMedicamentos():
    global usuarios
    nombre = request.json["nombre"]
    precio = request.json["precio"]
    descripcion = request.json["descripcion"]
    cantidad = request.json["cantidad"]
    nuevo_medicamento = Medicamento(nombre, precio, descripcion, cantidad)
    usuarios.append(nuevo_medicamento)
    return jsonify({'Mensaje':'Se agregó el medicamento exitosamente'})

@app.route('/Eliminar/<string:username>', methods = ['DELETE'])
def eliminarUsuario(username):
    if request.method == 'DELETE':
        for i in range(len(usuarios)-1):
            if username == usuarios[i].getUser_name():
                del usuarios[i]
                objeto = {'Mensaje': 'Usuario eliminado exitosamente'}
                break
            else:
                objeto = {'Mensaje': 'El usuario a eliminar no se encontró'}
    return(jsonify(objeto))

@app.route('/Eliminar/Medicamentos/<string:medicamento>', methods = ['DELETE'])
def eliminarMedicamento(medicamento):
    if request.method == 'DELETE':
        for i in range(len(medicamentos)-1):
            if medicamento == medicamentos[i].getNombre():
                del medicamentos[i]
                objeto = {'Mensaje': 'Medicamento eliminado exitosamente'}
                break
            else:
                objeto = {'Mensaje': 'El medicamento a eliminar no se encontró'}
    return(jsonify(objeto))

if __name__ =="__main__":
    app.run(host = "0.0.0.0", port = 3000, debug=True)