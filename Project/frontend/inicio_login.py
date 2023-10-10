import sys
from Login import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class InicioLogin(QMainWindow):
    def __init__(self):
        super(InicioLogin, self).__init__()
        self.ui = Ui_ventana_principal()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # Quita el marco de la ventana y mantiene en la parte superior
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.panel_principal.setStyleSheet("#panel_principal{border-radius:15px;}")
        self.ui.panel_izquierda.setStyleSheet("#panel_izquierda{border-top-left-radius: 15px; border-bottom-left-radius: 15px;}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InicioLogin()
    window.show()
    sys.exit(app.exec_())