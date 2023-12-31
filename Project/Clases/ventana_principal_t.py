import sys
from SRC.iconos import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent
from UI.ventana_principal_trabajo import *


class ventana_principal_trabajo(QMainWindow):
    def __init__(self):
        super(ventana_principal_trabajo, self).__init__()
        self.ui = Ui_ventana_de_trabajo()
        self.ui.setupUi(self)
        self.ui.btn_cerrar.setIcon(QIcon(":/icons/img_cerrar.svg"))
        self.ui.btn_cerrar.setIconSize(QSize(25, 25))
        self.ui.btn_minimizar.setIcon(QIcon(":/icons/img_minimizar.svg"))
        self.ui.btn_minimizar.setIconSize(QSize(25, 25))
        self.ui.btn_maximizar.setIcon(QIcon(":/icons/maximizar.svg"))
        self.ui.btn_maximizar.setIconSize(QSize(25, 25))
        self.ui.btn_btn_menu.setIcon(QIcon(":/icons/menu.svg"))
        self.ui.btn_btn_cuenta.setIcon(QIcon(":/icons/cuenta.svg"))
        self.ui.btn_btn_buscar.setIcon(QIcon(":/icons/buscar.svg"))
        self.ui.btn_btn_buscar_proveedor.setIcon(QIcon(":/icons/buscar.svg"))

        self.ui.bts_bts_clientes.setIcon(QIcon(":icons/clientes.svg"))
        self.ui.bts_bts_compras.setIcon(QIcon(":icons/compras.svg"))
        self.ui.bts_bts_inventario.setIcon(QIcon(":icons/inventario.svg"))
        self.ui.bts_bts_proveedor.setIcon(QIcon(":icons/proveedor.svg"))
        self.ui.bts_bts_venta.setIcon(QIcon(":icons/venta.svg"))
        self.ui.bts_bts_empleados.setIcon(QIcon(":icons/users.svg"))
        self.ui.bts_bts_empleados.setText("Empleados")

        self.ui.img_logo.setPixmap(QPixmap(":icons/Dev_Rous_SF.png"))
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.btn_cerrar.clicked.connect(self.cerrar)
        self.ui.btn_minimizar.clicked.connect(self.minimizar)
        self.ui.btn_maximizar.clicked.connect(self.maximizar)

        self.ui.btn_btn_menu.clicked.connect(self.expan_ocul_menu_desple)

        self.ui.btn_btn_cuenta.clicked.connect(self.panel_cuenta)
        self.ui.bts_bts_venta.clicked.connect(self.panel_venta)
        self.ui.bts_bts_inventario.clicked.connect(self.panel_inventario)
        self.ui.bts_bts_clientes.clicked.connect(self.panel_clientes)
        self.ui.bts_bts_proveedor.clicked.connect(self.panel_proveedores)
        self.ui.bts_bts_compras.clicked.connect(self.panel_compras)
        self.ui.bts_bts_empleados.clicked.connect(self.panel_empleados)


        self.ui.panel_opciones_desplegable.setStyleSheet("max-width:90px;")

        
        self.ui.panel_opciones_desplegable.hide()
        self.ui.panel_paginas.setCurrentIndex(1)

    # index 1 es el logo
    def expan_ocul_menu_desple(self):
        if not self.ui.panel_opciones_desplegable.isVisible():
            self.ui.panel_opciones_desplegable.show()
        else:
            self.ui.panel_opciones_desplegable.hide()

    def panel_cuenta(self):
        self.ui.panel_paginas.setCurrentIndex(0)

    def panel_venta(self):
        self.ui.panel_paginas.setCurrentIndex(4)

    def panel_inventario(self):
        self.ui.panel_paginas.setCurrentIndex(6)

    def panel_clientes(self):
        self.ui.panel_paginas.setCurrentIndex(3)

    def panel_proveedores(self):
        self.ui.panel_paginas.setCurrentIndex(5)

    def panel_compras(self):
        self.ui.panel_paginas.setCurrentIndex(2)

    def panel_empleados(self):
        self.ui.panel_paginas.setCurrentIndex(7)

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
            self.drag_start_position = (
                event.globalPos() - self.frameGeometry().topLeft()
            )

    def mouseMoveEvent(self, event: QMouseEvent):
        if not self.isFullScreen() and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ventana_principal_trabajo()
    ui.show()
    sys.exit(app.exec_())
