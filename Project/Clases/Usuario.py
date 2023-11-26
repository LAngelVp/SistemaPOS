from Base_de_Datos.Conection import *
class Usuario:
    def __init__(self):
        pass
    
    def conectar(self):
        conexion_bd = ConexionBD()
        cursor = conexion_bd.conectar()
        
        if cursor is not None:
            cursor.execute("SELECT * FROM Usuarios")
            resultados = cursor.fetchall()
            if len(resultados) == 0:
                print ("No se encuentran elementos")
            else:
                for fila in resultados:
                    print(fila)
            cursor.close()
            conexion_bd.conectame.close()
        else:
            print("No se pudo conectar a la base de datos")

