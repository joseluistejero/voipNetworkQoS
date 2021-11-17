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
        VentanaWindow.resize(838, 780)
        self.centralwidget = QtWidgets.QWidget(VentanaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.pbCalcular.setGeometry(QtCore.QRect(300, 390, 211, 41))
        self.pbCalcular.setObjectName("pbCalcular")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 140, 811, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(11)
        VentanaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 26))
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
        self.pbCalcular.setText(_translate("VentanaWindow", "Calcular"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("VentanaWindow", "CODEC"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VentanaWindow", "MOS"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("VentanaWindow", "RT"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("VentanaWindow", "BHT"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("VentanaWindow", "Nll"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("VentanaWindow", "BWll"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("VentanaWindow", "BWst"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("VentanaWindow", "PaquetesRTP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaWindow = QtWidgets.QMainWindow()
    ui = Ui_VentanaWindow()
    ui.setupUi(VentanaWindow)
    VentanaWindow.show()
    sys.exit(app.exec_())

