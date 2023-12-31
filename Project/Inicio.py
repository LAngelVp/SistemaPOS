import sys
from iconos import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent
from frontend.Login import *
from Clases.ventana_principal_t import *
from Clases.Base_de_Datos.Conection import ConexionBD


class Inicio(QMainWindow):
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_ventana_principal()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.panel_principal.setStyleSheet("border-radius: 12px;")
        self.ui.panel_izquierda.setStyleSheet(
            "background:#edecec; border-top-right-radius:0px; border-bottom-right-radius:0px;"
        )
        self.ui.btn_cerrar.setIconSize(QSize(24,24))
        self.ui.lbr_recuperar_credenciales.setStyleSheet("text-decoration: underline")
        self.ui.btn_cerrar.setIcon(QIcon(":/icons/img_cerrar.svg"))
        self.ui.btn_cerrar.clicked.connect(self.cerrar)
        self.ui.btn_ingresar.clicked.connect(self.ingresar)
        ConexionBD().conexion

    def cerrar(self):
        self.close()

    def ingresar(self):
        self.usuario = self.ui.txt_usuario.text()
        self.contraseña = self.ui.txt_contrasena.text()
        self.connect = ConexionBD().conexion
        query = "SELECT * FROM usuarios WHERE nombre_usuario = %s AND contraseña = %s"
        datos = (self.usuario, self.contraseña)
        self.cursor = self.connect.cursor()
        self.cursor.execute(query, datos)
        resultado = self.cursor.fetchone()
        self.cursor.close()
        ConexionBD().cerrar_conexion

        if resultado:
            self.ui = ventana_principal_trabajo()
            self.close()
            self.ui.show()
        else:
            self.ui.lbl_datos_incorrectos.setText("Usuario o contraseña incorrectos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Inicio()
    ui.show()
    sys.exit(app.exec_())
