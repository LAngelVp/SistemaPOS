import sys
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
from PyQt5.QtGui import QIcon
from SRC.iconos import *


class Mensajes_pop(QWidget):
    def __init__(self, titulo=None, mensaje=None):
        self.titulo = titulo
        self.mensaje = mensaje

    def contenido_vacio(self):
        componente = QMessageBox()
        componente.setWindowIcon(QIcon(':/Source/alarma.png'))
        componente.setWindowTitle(self.titulo)
        componente.setIcon(QMessageBox.Warning)
        componente.setText(self.mensaje)
        componente.setStandardButtons(
            QMessageBox.Ok
        )
        componente.setDefaultButton(QMessageBox.Save)
        componente.exec()
