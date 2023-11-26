from Base_de_Datos.Conection import *
class Persona:
    def __init__(self,nombre, fecha_nacimiento , numero_identificacion, direccion, correo_electronico, numero_telefono, localidad, estado):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.numero_identificacion = numero_identificacion
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.numero_telefono = numero_telefono
        self.localidad = localidad
        self.estado = estado

    def agregar_persona(self):
        pass

