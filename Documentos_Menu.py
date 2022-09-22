# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documentos_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_documentos_menu(object):
    def setupUi(self, documentos_menu):
        documentos_menu.setObjectName("documentos_menu")
        documentos_menu.resize(1290, 841)
        documentos_menu.setMinimumSize(QtCore.QSize(1290, 841))
        documentos_menu.setMaximumSize(QtCore.QSize(1290, 841))
        documentos_menu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(documentos_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Borda = QtWidgets.QLabel(self.centralwidget)
        self.Label_Borda.setGeometry(QtCore.QRect(0, 783, 1290, 18))
        self.Label_Borda.setText("")
        self.Label_Borda.setPixmap(QtGui.QPixmap("Imagens/Borda.png"))
        self.Label_Borda.setScaledContents(True)
        self.Label_Borda.setObjectName("Label_Borda")
        self.botao_documentos_de_pecas02 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_documentos_de_pecas02.setGeometry(QtCore.QRect(180, 60, 911, 161))
        self.botao_documentos_de_pecas02.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(234, 229, 239);\n"
"border-width:7px;\n"
"font: 75 45pt \"Bosch Sans Bold\";\n"
"border-radius: 30px;")
        self.botao_documentos_de_pecas02.setObjectName("botao_documentos_de_pecas02")
        self.botao_documentos_de_pecas01 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_documentos_de_pecas01.setGeometry(QtCore.QRect(50, 40, 200, 200))
        self.botao_documentos_de_pecas01.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(155, 228, 179);\n"
"border-width:7px;\n"
"border-radius: 100px;\n"
"font: 75 50pt \"Bosch Sans Bold\";")
        self.botao_documentos_de_pecas01.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/Documentos.Peças.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_documentos_de_pecas01.setIcon(icon)
        self.botao_documentos_de_pecas01.setIconSize(QtCore.QSize(125, 125))
        self.botao_documentos_de_pecas01.setObjectName("botao_documentos_de_pecas01")
        self.botao_diagrama_eletrico02 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_diagrama_eletrico02.setGeometry(QtCore.QRect(180, 310, 911, 161))
        self.botao_diagrama_eletrico02.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(234, 229, 239);\n"
"border-width:7px;\n"
"font: 75 45pt \"Bosch Sans Bold\";\n"
"border-radius: 30px;")
        self.botao_diagrama_eletrico02.setObjectName("botao_diagrama_eletrico02")
        self.botao_diagrama_eletrico01 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_diagrama_eletrico01.setGeometry(QtCore.QRect(50, 290, 200, 200))
        self.botao_diagrama_eletrico01.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 207, 0);\n"
"border-width:7px;\n"
"border-radius: 100px;\n"
"font: 75 50pt \"Bosch Sans Bold\";")
        self.botao_diagrama_eletrico01.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagens/Diagrama_eletrico.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_diagrama_eletrico01.setIcon(icon1)
        self.botao_diagrama_eletrico01.setIconSize(QtCore.QSize(160, 160))
        self.botao_diagrama_eletrico01.setObjectName("botao_diagrama_eletrico01")
        self.botao_mae02 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_mae02.setGeometry(QtCore.QRect(180, 570, 911, 161))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans Bold")
        font.setPointSize(45)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.botao_mae02.setFont(font)
        self.botao_mae02.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_mae02.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(234, 229, 239);\n"
"border-width:7px;\n"
"font: 75 45pt \"Bosch Sans Bold\";\n"
"border-radius: 30px;")
        self.botao_mae02.setCheckable(False)
        self.botao_mae02.setObjectName("botao_mae02")
        self.botao_mae01 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_mae01.setGeometry(QtCore.QRect(50, 550, 200, 200))
        self.botao_mae01.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(101, 106, 111);\n"
"border-width:7px;\n"
"border-radius: 100px;\n"
"font: 75 50pt \"Bosch Sans Bold\";")
        self.botao_mae01.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagens/MAE.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_mae01.setIcon(icon2)
        self.botao_mae01.setIconSize(QtCore.QSize(160, 160))
        self.botao_mae01.setObjectName("botao_mae01")
        self.botao_home = QtWidgets.QPushButton(self.centralwidget)
        self.botao_home.setGeometry(QtCore.QRect(1150, 10, 120, 120))
        self.botao_home.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;")
        self.botao_home.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagens/Home.Documentos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_home.setIcon(icon3)
        self.botao_home.setIconSize(QtCore.QSize(105, 105))
        self.botao_home.setObjectName("botao_home")
        documentos_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(documentos_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.menubar.setObjectName("menubar")
        documentos_menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(documentos_menu)
        self.statusbar.setObjectName("statusbar")
        documentos_menu.setStatusBar(self.statusbar)

        self.retranslateUi(documentos_menu)
        QtCore.QMetaObject.connectSlotsByName(documentos_menu)

    def retranslateUi(self, documentos_menu):
        _translate = QtCore.QCoreApplication.translate
        documentos_menu.setWindowTitle(_translate("documentos_menu", "MainWindow"))
        self.botao_documentos_de_pecas02.setText(_translate("documentos_menu", "  DOCUMENTOS DE PEÇAS"))
        self.botao_diagrama_eletrico02.setText(_translate("documentos_menu", "  DIAGRAMA ELÉTRICO     "))
        self.botao_mae02.setText(_translate("documentos_menu", "  MAPA DE RISCOS            "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    documentos_menu = QtWidgets.QMainWindow()
    ui = Ui_documentos_menu()
    ui.setupUi(documentos_menu)
    documentos_menu.show()
    sys.exit(app.exec_())
