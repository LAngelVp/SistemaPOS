import mysql.connector
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
                self.connect_me = mysql.connector.connect(
                    host=self.host, user=self.user, password=self.password, database=self.database
                )
                print("Conexión exitosa a la base de datos")
            except mysql.connector.Error as err:
                print(f"Error en la conexión a la base de datos: {err}")
        return self.connect_me
    @property
    def cerrar_conexion(self):
        if self.connect_me is not None:
            self.connect_me.close()
            print("Conexión cerrada")