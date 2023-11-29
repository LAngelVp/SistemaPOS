import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent
from SRC.iconos import *
from UI.RegistroPersonal import *
from Mensajes_emergentes import *


class Inicio(QMainWindow):
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_Registro_Personal()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.w_principal.setStyleSheet("border-radius: 12px;")
        self.ui.img_empleado.setStyleSheet("border-radius: 0px;")
        self.ui.btn_cerrar.setIcon(QIcon(":/Source/img_cerrar.svg"))
        self.ui.btn_minimizar.setIcon(QIcon(":/Source/img_minimizar.svg"))
        self.ui.btn_cerrar.clicked.connect(self.cerrar)

        # COMMENT: BOTONES
        self.ui.btn_agregar_foto.clicked.connect(self.agregar_foto)
        self.ui.btn_eliminar_foto.clicked.connect(self.eliminar_foto)
        self.ui.btn_mostrar_cv.clicked.connect(self.mostrar_cv)
        self.ui.btn_agregar_cv.clicked.connect(self.agregar_cv)
        self.ui.btn_eliminar_cv.clicked.connect(self.eliminar_cv)
        self.ui.btn_cancelar_personal.clicked.connect(self.cancelar_registro_personal)
        self.ui.btn_guardarpersonal.clicked.connect(self.guardar_persona)

    def comprobar_txt(self):
        txts = [
            self.ui.txt_id,
            self.ui.txt_nmbre,
            self.ui.txt_identificacion,
            self.ui.txt_direccion,
            self.ui.txt_correo,
            self.ui.txt_telefono,
            self.ui.txt_nss,
            self.ui.txt_localidad,
            self.ui.txt_estado,
            self.ui.txt_nombre_usuario,
            self.ui.txt_contra_usuario,
            self.ui.txt_nombre_contacto,
            self.ui.txt_nombre_contacto2,
            self.ui.txt_numero_contacto1,
            self.ui.txt_numero_contacto2,
            self.ui.lbl_fotografia
        ]
        for i in txts:
            if i.text().strip() == "":
                return Mensajes_pop("Elementos vacios", "Todos los elementos del formulario deben de ir completamente rellenos.").contenido_vacio()
            else:
                print("error")
        
        
    def agregar_foto(self):
        self.comprobar_txt()
    def eliminar_foto(self):
        pass
    def mostrar_cv(self):
        pass
    def agregar_cv(self):
        pass
    def eliminar_cv(self):
        pass
    def cancelar_registro_personal(self):
        pass
    def guardar_persona(self):
        pass


    def cerrar(self):
        self.close()
        # Mensajes_pop("Mensaje de alerta", "Esta es una prueba").contenido_vacio()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Inicio()
    ui.show()
    sys.exit(app.exec_())
