from Conection import ConexionBD
from Persona import *
class Empleado(Persona):
    def __init__(self, curriculum_vitae, numero_seguro_social, nombre_usuario, contraseña, foto):
        super().__init__(nombre, fecha_nacimiento , numero_identificacion, direccion, correo_electronico, numero_telefono, localidad, estado)

        self.curriculum_vitae = curriculum_vitae
        self.numero_seguro_social = numero_seguro_social
        self.nombre_usuario = nombre_usuario
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.foto = foto
    
    def agregar_empleado(self, nombre, fecha_nacimiento , numero_identificacion, direccion, correo_electronico, numero_telefono, localidad, estado, curriculum_vitae, numero_seguro_social, nombre_usuario, contraseña, foto):
        

        pass
#         try:
#             con = ConexionBD().conexion
#             query = "INSERT INTO empleado (nombre, fecha_nacimiento, genero, direccion, telefono, tipo_de_sangre, puesto, salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#             values = (self.full_name, self.date_of_birth, self.gender, self.address, self.phone, self.blood_of_type, self.stand, self.salary)
#             cursor = con.cursor()
#             cursor.execute(query, values)
#             con.commit()
#             ConexionBD().cerrar_conexion
#         except:
#             print ("Error en la conexion de la base de datos")

# empleado = Empleado("Luis Angel", "1996-10-31", "masculino", "paso del macho", "212-123-12-21", "0-", "ingeniero", 1200)
# empleado.add_user()

