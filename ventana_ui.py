# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_iu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaWindow(object):
    def setupUi(self, VentanaWindow):
        VentanaWindow.setObjectName("VentanaWindow")
        VentanaWindow.resize(838, 772)
        self.centralwidget = QtWidgets.QWidget(VentanaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(0, 530, 791, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gbTopologia = QtWidgets.QGroupBox(self.centralwidget)
        self.gbTopologia.setEnabled(True)
        self.gbTopologia.setGeometry(QtCore.QRect(20, 300, 751, 141))
        self.gbTopologia.setObjectName("gbTopologia")
        self.iCodecs = QtWidgets.QComboBox(self.gbTopologia)
        self.iCodecs.setEnabled(True)
        self.iCodecs.setGeometry(QtCore.QRect(280, 10, 171, 22))
        self.iCodecs.setObjectName("iCodecs")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 751, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setEnabled(True)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 691, 215))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lNC = QtWidgets.QLabel(self.formLayoutWidget)
        self.lNC.setEnabled(True)
        self.lNC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lNC.setObjectName("lNC")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lNC)
        self.iNC = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.iNC.setEnabled(True)
        self.iNC.setObjectName("iNC")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iNC)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setEnabled(True)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pbCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.pbCalcular.setGeometry(QtCore.QRect(30, 630, 211, 41))
        self.pbCalcular.setObjectName("pbCalcular")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(420, 620, 111, 21))
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(110, 460, 181, 21))
        self.checkBox.setObjectName("checkBox")
        self.lPruebas = QtWidgets.QLabel(self.centralwidget)
        self.lPruebas.setEnabled(True)
        self.lPruebas.setGeometry(QtCore.QRect(40, 10, 101, 21))
        self.lPruebas.setObjectName("lPruebas")
        self.iPruebas = QtWidgets.QLineEdit(self.centralwidget)
        self.iPruebas.setEnabled(True)
        self.iPruebas.setGeometry(QtCore.QRect(200, 10, 113, 20))
        self.iPruebas.setObjectName("iPruebas")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(320, 460, 109, 32))
        self.pushButton.setObjectName("pushButton")
        VentanaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 24))
        self.menubar.setObjectName("menubar")
        VentanaWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaWindow)
        self.statusbar.setObjectName("statusbar")
        VentanaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaWindow)
        QtCore.QMetaObject.connectSlotsByName(VentanaWindow)

    def retranslateUi(self, VentanaWindow):
        _translate = QtCore.QCoreApplication.translate
        VentanaWindow.setWindowTitle(_translate("VentanaWindow", "MainWindow"))
        self.gbTopologia.setTitle(_translate("VentanaWindow", "Topología"))
        self.lNC.setText(_translate("VentanaWindow", "Número de clientes:"))
        self.label.setText(_translate("VentanaWindow", "TextLabel"))
        self.label_2.setText(_translate("VentanaWindow", "TextLabel"))
        self.label_3.setText(_translate("VentanaWindow", "TextLabel"))
        self.label_4.setText(_translate("VentanaWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("VentanaWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("VentanaWindow", "Tab 2"))
        self.pbCalcular.setText(_translate("VentanaWindow", "Calcular"))
        self.radioButton.setText(_translate("VentanaWindow", "RadioButton"))
        self.checkBox.setText(_translate("VentanaWindow", "CheckBox"))
        self.lPruebas.setText(_translate("VentanaWindow", "TextLabel"))
        self.pushButton.setText(_translate("VentanaWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaWindow = QtWidgets.QMainWindow()
    ui = Ui_VentanaWindow()
    ui.setupUi(VentanaWindow)
    VentanaWindow.show()
    sys.exit(app.exec_())
