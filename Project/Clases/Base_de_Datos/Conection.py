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

        # COMMENT: TABLA DE PROVEEDOR
        tabla_proveedor = """CREATE TABLE IF NOT EXISTS proveedores(
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(255),
        numero_telefonico VARCHAR(10),
        correo VARCHAR(255),
        numero_identificacion_federal VARCHAR(255),
        cuenta_bancaria VARCHAR(255),
        plazos_pago FLOAT,
        categoria VARCHAR(255),
        comentarios TEXT,
        lista_productos_suministrados FLOAT,
        documentos_adjuntos BLOB
        )"""
        # COMMENT: TABLA PUESTOS
        tabla_puesto = """CREATE TABLE IF NOT EXISTS puestos(
        id INTEGER PRIMARY KEY,
        nombre_puesto VARCHAR(100),
        sueldo FLOAT
        )"""
        # COMMENT: TABLA USUARIOS
        tabla_usuario = """CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre_usuario VARCHAR(50),
        contraseña VARCHAR(25)
        )"""
        # COMMENT: TABLA CONTACTO EMERGENCIA
        tabla_contacto_emergencia = """CREATE TABLE IF NOT EXISTS contactos_emergencia (
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(255),
        parentezco VARCHAR(50),
        numero_telefono VARCHAR(10)
        )"""
        
        # ---------------------------------------------------------------
        # COMMENT: TABLAS CON LLAVES FORANEAS ---------------------------
        # COMMENT: TABLA DE COMPRAS
        tabla_compras = """CREATE TABLE IF NOT EXISTS compras(
        id INTEGER PRIMARY KEY,
        fecha_compra DATE,
        id_proveedor INTEGER,
        total_compra FLOAT,
        metodo_pago VARCHAR(50),
        numero_factura VARCHAR(100),
        comentarios TEXT,
        FOREIGN KEY (id_proveedor) REFERENCES proveedores(id)
        )"""
        # COMMENT: TABLA PRODUCTOS
        tabla_productos = """CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY,
        codigo_barras VARCHAR(255),
        nombre VARCHAR(255),
        categoria VARCHAR(100),
        precio_venta FLOAT,
        costo_adquisicion FLOAT,
        cantidad_inventario INTEGER,
        descripcion TEXT,
        unidad_medida TEXT,
        id_proveedor INTEGER,
        FOREIGN KEY (id_proveedor) REFERENCES proveedores(id)
        )"""
        #COMMENT: TABLA DE DETALLE DE COMPRA
        tabla_detalle_compra = """CREATE TABLE IF NOT EXISTS detalle_compra(
        id INTEGER PRIMARY KEY,
        id_compra INTEGER,
        id_producto INTEGER,
        cantidad INTEGER,
        precio_unitario FLOAT,
        FOREIGN KEY (id_compra) REFERENCES compras(id),
        FOREIGN KEY (id_producto) REFERENCES productos(id)
        )"""
        # COMMENT: TABLA EMPLEADOS
        tabla_empleados = """CREATE TABLE IF NOT EXISTS empleados(
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(255),
        fecha_nacimiento DATE,
        numero_identificacion VARCHAR(13),
        direccion TEXT,
        correo_electronico VARCHAR(100),
        numero_telefonico VARCHAR(10),
        curriculum_vitae BLOB,
        numero_seguro_social VARCHAR(11),
        localidad VARCHAR(50),
        estado VARCHAR(50),
        foto BLOB,
        puesto_id INTEGER,
        sueldo FLOAT,
        usuario_id INTEGER,
        contacto_emergencia_id INTEGER,
        FOREIGN KEY (puesto_id) REFERENCES puestos(id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (contacto_emergencia_id) REFERENCES contactos_emergencia(id)
        )"""
        #--------------------------------------------------
        #COMMENT: EJECUCION DE LAS TABLAS SIN LLAVE FORANEA
        cursor.execute(tabla_proveedor)
        cursor.execute(tabla_puesto)
        cursor.execute(tabla_usuario)
        cursor.execute(tabla_contacto_emergencia)
        #---------------------------------------------------
        #COMMENT: EJECUCION DE LAS TABLAS CON LLAVES FORANEAS
        cursor.execute(tabla_productos)
        cursor.execute(tabla_compras)
        cursor.execute(tabla_detalle_compra)
        cursor.execute(tabla_empleados)

        self.conexion.commit()
        self.cerrar_conexion


ConexionBD().crear_tablas
