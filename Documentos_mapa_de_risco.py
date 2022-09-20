# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documentos_mapa_de_risco.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mapa_de_riscos(object):
    def setupUi(self, mapa_de_riscos):
        mapa_de_riscos.setObjectName("mapa_de_riscos")
        mapa_de_riscos.resize(1290, 841)
        mapa_de_riscos.setMinimumSize(QtCore.QSize(1290, 841))
        mapa_de_riscos.setMaximumSize(QtCore.QSize(1290, 841))
        mapa_de_riscos.setStyleSheet("background-color: rgb(255, 255, 255);")
        mapa_de_riscos.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(mapa_de_riscos)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Borda = QtWidgets.QLabel(self.centralwidget)
        self.Label_Borda.setGeometry(QtCore.QRect(0, 783, 1290, 18))
        self.Label_Borda.setText("")
        self.Label_Borda.setPixmap(QtGui.QPixmap("Imagens/Borda.png"))
        self.Label_Borda.setScaledContents(True)
        self.Label_Borda.setObjectName("Label_Borda")
        self.botao_home = QtWidgets.QPushButton(self.centralwidget)
        self.botao_home.setGeometry(QtCore.QRect(1150, 10, 120, 120))
        self.botao_home.setStyleSheet("\n"
"border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;\n"
"font: 75 65pt \"Bosch Sans Bold\";\n"
"border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.botao_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/Home.Documentos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_home.setIcon(icon)
        self.botao_home.setIconSize(QtCore.QSize(105, 105))
        self.botao_home.setObjectName("botao_home")
        self.label_imagem = QtWidgets.QLabel(self.centralwidget)
        self.label_imagem.setGeometry(QtCore.QRect(30, 150, 1231, 611))
        self.label_imagem.setStyleSheet("")
        self.label_imagem.setObjectName("label_imagem")
        self.label_MAE = QtWidgets.QPushButton(self.centralwidget)
        self.label_MAE.setGeometry(QtCore.QRect(20, 0, 141, 141))
        self.label_MAE.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;\n"
"font: 75 65pt \"Bosch Sans Bold\";\n"
"border-radius: 70px;\n"
"background-color: rgb(132, 134, 137);")
        self.label_MAE.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagens/Documentos.MAE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.label_MAE.setIcon(icon1)
        self.label_MAE.setIconSize(QtCore.QSize(95, 95))
        self.label_MAE.setObjectName("label_MAE")
        mapa_de_riscos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mapa_de_riscos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.menubar.setObjectName("menubar")
        mapa_de_riscos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mapa_de_riscos)
        self.statusbar.setObjectName("statusbar")
        mapa_de_riscos.setStatusBar(self.statusbar)

        self.retranslateUi(mapa_de_riscos)
        QtCore.QMetaObject.connectSlotsByName(mapa_de_riscos)

    def retranslateUi(self, mapa_de_riscos):
        _translate = QtCore.QCoreApplication.translate
        mapa_de_riscos.setWindowTitle(_translate("mapa_de_riscos", "MainWindow"))
        self.label_imagem.setText(_translate("mapa_de_riscos", "imagem"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mapa_de_riscos = QtWidgets.QMainWindow()
    ui = Ui_mapa_de_riscos()
    ui.setupUi(mapa_de_riscos)
    mapa_de_riscos.show()
    sys.exit(app.exec_())
