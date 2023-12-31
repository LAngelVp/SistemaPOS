# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\luis_\Desktop\ProyectosPersonales\PosSystem\Project\frontend\Recuperacion.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_panel_ventana_recuperacion(object):
    def setupUi(self, panel_ventana_recuperacion):
        panel_ventana_recuperacion.setObjectName("panel_ventana_recuperacion")
        panel_ventana_recuperacion.setWindowModality(QtCore.Qt.NonModal)
        panel_ventana_recuperacion.resize(320, 336)
        panel_ventana_recuperacion.setMinimumSize(QtCore.QSize(300, 300))
        panel_ventana_recuperacion.setMaximumSize(QtCore.QSize(320, 336))
        panel_ventana_recuperacion.setStyleSheet("#panel_ventana_recuperacion{\n"
"max-width: 320px;\n"
"min-width:300px;\n"
"}\n"
"#panel_encabezado{\n"
"max-height:40px;\n"
"    background-color: rgb(204, 204, 204);\n"
"}\n"
"#panel_contenido_img{\n"
"max-height:120px;\n"
"}\n"
"#panel_img{\n"
"max-width:150px;\n"
"}\n"
"#panel_contenido_interno{\n"
"max-width: 350px;\n"
"}\n"
"#lbm_lbm_correoerroneo{\n"
"font_size:8px;\n"
"font_family:Arial;\n"
"}\n"
"[objectName^=\"btn_btn\"] {\n"
"background-color: rgb(204, 204, 204);\n"
"    color: rgb(255, 255, 255);\n"
" border-radius: 4px;\n"
" min-height: 25px;\n"
" max-height: 35px;\n"
" font-size:14px;\n"
" font-family: Arial;\n"
"font-weight: bold;\n"
"}\n"
"[objectName^=\"btc_btc\"] {\n"
"background-color:transparent;\n"
"}\n"
"[objectName^=\"lbl_lbl\"] {\n"
" font-size:14px;\n"
" font-family: Arial;\n"
"}\n"
"[objectName^=\"txt_txt\"] {\n"
" font-size:14px;\n"
" font-family: Arial;\n"
"}\n"
"#btn_btn_modificar{\n"
"background-color: rgb(0, 102, 204);\n"
"}\n"
"#btn_btn_modificar:hover{\n"
"background-color: rgb(0, 109, 155);\n"
"}\n"
"#btn_btn_aceptar{\n"
"background-color: rgb(97, 188, 132);\n"
"}\n"
"#btn_btn_aceptar:hover{\n"
"    background-color: rgb(46, 139, 87);\n"
"}")
        self.panel_central = QtWidgets.QWidget(panel_ventana_recuperacion)
        self.panel_central.setObjectName("panel_central")
        self.gridLayout = QtWidgets.QGridLayout(self.panel_central)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.panel_cuerpo = QtWidgets.QWidget(self.panel_central)
        self.panel_cuerpo.setMinimumSize(QtCore.QSize(0, 0))
        self.panel_cuerpo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.panel_cuerpo.setObjectName("panel_cuerpo")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.panel_cuerpo)
        self.gridLayout_3.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.panel_encabezado = QtWidgets.QWidget(self.panel_cuerpo)
        self.panel_encabezado.setObjectName("panel_encabezado")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.panel_encabezado)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(253, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btc_btc_minimizar = QtWidgets.QPushButton(self.panel_encabezado)
        self.btc_btc_minimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btc_btc_minimizar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\luis_\\Desktop\\ProyectosPersonales\\PosSystem\\Project\\frontend\\../../../../../Downloads/minimizar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btc_btc_minimizar.setIcon(icon)
        self.btc_btc_minimizar.setIconSize(QtCore.QSize(20, 20))
        self.btc_btc_minimizar.setObjectName("btc_btc_minimizar")
        self.horizontalLayout.addWidget(self.btc_btc_minimizar)
        self.btc_btc_cerrar = QtWidgets.QPushButton(self.panel_encabezado)
        self.btc_btc_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btc_btc_cerrar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\luis_\\Desktop\\ProyectosPersonales\\PosSystem\\Project\\frontend\\../../../../../Downloads/img_cerrar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btc_btc_cerrar.setIcon(icon1)
        self.btc_btc_cerrar.setIconSize(QtCore.QSize(20, 20))
        self.btc_btc_cerrar.setObjectName("btc_btc_cerrar")
        self.horizontalLayout.addWidget(self.btc_btc_cerrar)
        self.gridLayout_3.addWidget(self.panel_encabezado, 0, 0, 1, 1)
        self.panel_contenido_img = QtWidgets.QWidget(self.panel_cuerpo)
        self.panel_contenido_img.setObjectName("panel_contenido_img")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.panel_contenido_img)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.panel_img = QtWidgets.QWidget(self.panel_contenido_img)
        self.panel_img.setMinimumSize(QtCore.QSize(0, 100))
        self.panel_img.setMaximumSize(QtCore.QSize(150, 16777215))
        self.panel_img.setObjectName("panel_img")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.panel_img)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img = QtWidgets.QLabel(self.panel_img)
        self.img.setText("")
        self.img.setTextFormat(QtCore.Qt.AutoText)
        self.img.setPixmap(QtGui.QPixmap("c:\\Users\\luis_\\Desktop\\ProyectosPersonales\\PosSystem\\Project\\frontend\\../../../../../Downloads/sign-question-icon_34359.png"))
        self.img.setScaledContents(True)
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setWordWrap(False)
        self.img.setObjectName("img")
        self.verticalLayout.addWidget(self.img)
        self.gridLayout_4.addWidget(self.panel_img, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.panel_contenido_img, 1, 0, 1, 1)
        self.panel_contenido = QtWidgets.QWidget(self.panel_cuerpo)
        self.panel_contenido.setObjectName("panel_contenido")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.panel_contenido)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.panel_contenido_interno = QtWidgets.QWidget(self.panel_contenido)
        self.panel_contenido_interno.setMaximumSize(QtCore.QSize(350, 16777215))
        self.panel_contenido_interno.setObjectName("panel_contenido_interno")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.panel_contenido_interno)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.panel_botones = QtWidgets.QWidget(self.panel_contenido_interno)
        self.panel_botones.setObjectName("panel_botones")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.panel_botones)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.btn_btn_modificar = QtWidgets.QPushButton(self.panel_botones)
        self.btn_btn_modificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_btn_modificar.setObjectName("btn_btn_modificar")
        self.verticalLayout_2.addWidget(self.btn_btn_modificar)
        self.btn_btn_aceptar = QtWidgets.QPushButton(self.panel_botones)
        self.btn_btn_aceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_btn_aceptar.setObjectName("btn_btn_aceptar")
        self.verticalLayout_2.addWidget(self.btn_btn_aceptar)
        self.gridLayout_5.addWidget(self.panel_botones, 3, 0, 1, 2)
        self.lbm_lbm_correoerroneo = QtWidgets.QLabel(self.panel_contenido_interno)
        self.lbm_lbm_correoerroneo.setText("")
        self.lbm_lbm_correoerroneo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbm_lbm_correoerroneo.setObjectName("lbm_lbm_correoerroneo")
        self.gridLayout_5.addWidget(self.lbm_lbm_correoerroneo, 2, 0, 1, 2)
        self.lbl_lbl_correo = QtWidgets.QLabel(self.panel_contenido_interno)
        self.lbl_lbl_correo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_lbl_correo.setObjectName("lbl_lbl_correo")
        self.gridLayout_5.addWidget(self.lbl_lbl_correo, 0, 0, 1, 1)
        self.txt_txt_correo = QtWidgets.QLineEdit(self.panel_contenido_interno)
        self.txt_txt_correo.setObjectName("txt_txt_correo")
        self.gridLayout_5.addWidget(self.txt_txt_correo, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.panel_contenido_interno, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.panel_contenido, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.panel_cuerpo, 0, 0, 1, 1)
        panel_ventana_recuperacion.setCentralWidget(self.panel_central)

        self.retranslateUi(panel_ventana_recuperacion)
        QtCore.QMetaObject.connectSlotsByName(panel_ventana_recuperacion)

    def retranslateUi(self, panel_ventana_recuperacion):
        _translate = QtCore.QCoreApplication.translate
        panel_ventana_recuperacion.setWindowTitle(_translate("panel_ventana_recuperacion", "Restablecimiento"))
        self.btn_btn_modificar.setText(_translate("panel_ventana_recuperacion", "Recuperar"))
        self.btn_btn_aceptar.setText(_translate("panel_ventana_recuperacion", "Registrar"))
        self.lbl_lbl_correo.setText(_translate("panel_ventana_recuperacion", "Correo electronico"))
        self.txt_txt_correo.setPlaceholderText(_translate("panel_ventana_recuperacion", "correo.123@ejemplo.com"))
