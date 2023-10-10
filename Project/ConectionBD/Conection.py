import mysql.connector
class ConexionBD:
    def __init__(self):
        self.user = "root"
        self.password = "MySQL"
        self.host = "localhost"
        self.database = "POS_Venta"
    
    def conectar(self):
        try:
            self.conectame = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.conectame.cursor()
            print("Conexión exitosa")
            return self.cursor
        except mysql.connector.Error as err:
            print(f"Error de conexión a la base de datos: {err}")
            return None
