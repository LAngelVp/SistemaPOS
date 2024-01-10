from Base_de_Datos.Conection import ConexionBD
from Modelos.Persona import *
from Modelos.Puesto import *
from Modelos.Usuario import *
from Modelos.Contactos import *

class Empleado(Persona, Puesto, Usuario, Contactos):
    def __init__(
        self,nombre,fecha_nacimiento,numero_identificacion,direccion,correo_electronico,numero_telefono,localidad,estado,fotografia,puesto,sueldo,nombre_contacto,parentezco,numero_telefono_contacto,curriculum_vitae,numero_seguro_social):
        Persona.__init__(self, nombre,fecha_nacimiento,numero_identificacion,direccion,correo_electronico,numero_telefono,localidad,estado,fotografia)
        Puesto.__init__(self,puesto,sueldo)
        Contactos.__init__(self, nombre_contacto, parentezco, numero_telefono_contacto)
# COMMENT --- PROPIEDADES DE LA CLASE
        self.curriculum_vitae = curriculum_vitae
        self.numero_seguro_social = numero_seguro_social

    def guardar_empleado(self):
        

    


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
