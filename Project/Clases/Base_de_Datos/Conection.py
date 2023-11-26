# import mysql.connector
import pymysql


class ConexionBD:
    def __init__(self):
        self.user = "root"
        self.password = "MySQL"
        self.host = "localhost"
        self.database = "POS_Venta"
        self.connect_me = None  # Conexión inicialmente nula

    @property
    def conexion(self):
        if self.connect_me is None:
            try:
                self.connect_me = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )
                print("Conexión exitosa a la base de datos")
            except pymysql.Error as err:
                self.crear_db()
                self.conexion
        return self.connect_me

    @property
    def cerrar_conexion(self):
        if self.connect_me is not None:
            self.connect_me.close()
            print("Conexión cerrada")

    def crear_db(self):
        try:
            with pymysql.connect(
                host=self.host, user=self.user, password=self.password
            ) as conexion:
                with conexion.cursor() as cursor:
                    consulta = f"CREATE DATABASE IF NOT EXISTS {self.database}"
                    cursor.execute(consulta)
                    print("Creamos la tabla")
        except pymysql.Error as error:
            print("No se creo")

    @property
    def crear_tablas(self):
        conexion = self.conexion
        cursor = conexion.cursor()
        tabla_usuario = """CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre_usuario VARCHAR(50),
        contraseña VARCHAR(25)
        )"""
        tabla_empleados = """CREATE TABLE IF NOT EXISTS empleados(
        id INTEGER PRIMARY KEY,
        curriculum_vitae BLOB,
        numero_seguro_social VARCHAR(11),
        foto BLOB,
        nombre VARCHAR(255),
        fecha_nacimiento DATE,
        numero_identificacion VARCHAR(13),
        direccion TEXT,
        correo_electronico VARCHAR(100),
        numero_telefonico VARCHAR(10),
        localidad VARCHAR(50),
        estado VARCHAR(50),
        puesto_id INTEGER,
        sueldo FLOAT,
        usuario_id INTEGER,
        FOREIGN KEY (puesto_id) REFERENCES puestos(id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )"""
        tabla_puesto = """CREATE TABLE IF NOT EXISTS puestos(
        id INTEGER PRIMARY KEY,
        nombre_puesto VARCHAR(100),
        sueldo FLOAT
        )"""
        cursor.execute(tabla_usuario)
        cursor.execute(tabla_puesto)
        cursor.execute(tabla_empleados)
        self.conexion.commit()
        self.cerrar_conexion


ConexionBD().crear_tablas
