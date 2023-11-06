import sys
import img
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent
from .ventana_principal_trabajo import Ui_ventana_de_trabajo

class ventana_principal_trabajo(QMainWindow):
    def __init__(self):
        super(ventana_principal_trabajo, self).__init__()
        self.ui = Ui_ventana_de_trabajo()
        self.ui.setupUi(self)
        self.ui.btn_cerrar.setIcon(QIcon(":/Source/img_cerrar.svg"))
        self.ui.btn_minimizar.setIcon(QIcon(":/Source/img_minimizar.svg"))
        self.ui.btn_maximizar.setIcon(QIcon(":/Source/maximizar.svg"))
        self.ui.btn_menu.setIcon(QIcon(":/Source/menu.svg"))
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.img_cliente_superior.setPixmap(QPixmap(":/Source/clientes.svg"))
        self.ui.img_compras_superior.setPixmap(QPixmap(":/Source/compras.svg"))
        self.ui.img_inventario_superior.setPixmap(QPixmap(":/Source/inventario.svg"))
        self.ui.img_provedor_superior.setPixmap(QPixmap(":/Source/proveedor.svg"))
        self.ui.img_ventas_superior.setPixmap(QPixmap(":/Source/ventas.svg"))
        self.ui.btn_cerrar.clicked.connect(self.cerrar)
        self.ui.btn_minimizar.clicked.connect(self.minimizar)
        self.ui.btn_maximizar.clicked.connect(self.maximizar)

    def cerrar(self):
        self.close()

    def minimizar(self):
        self.showMinimized()

    def maximizar(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event: QMouseEvent):
        if not self.isFullScreen() and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ventana_principal_trabajo()
    ui.show()
    sys.exit(app.exec_())