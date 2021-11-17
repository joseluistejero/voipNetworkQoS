from PyQt5 import QtWidgets
from main_ui import *
from ventana_ui import *
import calculateCodec

class ResultsWindow(QtWidgets.QMainWindow, Ui_VentanaWindow):

    def __init__(self, result):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(len(result[i])):
                newitem = QtWidgets.QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i, j, newitem)

    


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.tabMenu.setCurrentIndex(0)
        self.pbCalcular.clicked.connect(self.goToSecondPage)

    def goToSecondPage(self):
        self.tabMenu.setCurrentIndex(1)
        self.progressBar.setValue(50)
        self.pbCalcular.clicked.connect(self.goToThirdPage)
        
    def goToThirdPage(self):
        self.tabMenu.setCurrentIndex(2)
        self.progressBar.setValue(75)
        self.pbCalcular.setText("Calcular")
        self.pbCalcular.clicked.connect(self.calcular)    

    def calcular(self):
        Nc=self.Nc.value();
        Nll=self.Nll.value();
        Tpll=self.Tpll.value();
        Pll=self.Pll.value();
        ETH=self.ETH.currentText();
        ENC=self.ENC.currentText();
        TUN=self.TUN.currentText();
        BWres=self.BWres.value();
        Rr=self.Rr.value();
        jitterMin=self.minJitter.value();
        jitterMax=self.maxJitter.value();
        mosString=self.MOS.currentText();
        TcWan=self.TcWan.currentText();
        Rto=self.Rt.currentText();
        if (mosString=="Excelente"):
            mos=5
        elif (mosString=="Buena"):
            mos=4
        elif (mosString=="Aceptable"):
            mos=3
        elif (mosString=="Pobre"):
            mos=2
        elif (mosString=="Mala"):
            mos=1
        else :
            mos=0
        
        if (Rto=="Aceptable"):
            Rt=150
        elif (Rto=="Moderadamente aceptable"):
            Rt==400
        
        stringTable=calculateCodec.calculateCodec(mos, Rr, jitterMin, jitterMax, Nc, Nll, Tpll, Pll, BWres, ETH, ENC, TcWan, Rt)
        self.w = ResultsWindow(stringTable)
        self.w.show()
        self.hide()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Pasar los parámetros
    windows = MainWindows()
    windows.show()
    app.exec_()