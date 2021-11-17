from PyQt5 import QtWidgets
from main_ui import *
from ventana_ui import *
import calculateCodec

class ResultsWindow(QtWidgets.QMainWindow, Ui_VentanaWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.lPruebas.setText("Aqui 2")
        self.pbCalcular.setText("Hacer cosas2")


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
        BWres=self.BWres.value();
        Rr=self.Rr.value();
        jitterMin=self.minJitter.value();
        jitterMax=self.maxJitter.value();
        mosString=self.MOS.currentText();
        ETH=self.ETH.currentText();
        ENC=self.ENC.currentText();
        TUN=self.TUN.currentText();
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
        #self.lPruebas.setText("Pos sa acabó")
        #self.tabWidget.setEnabled(1)
        #self.w = ResultsWindow()
        #self.w.show()
        #self.hide()
        calculateCodec.calculateCodec(mos, Rr, jitterMin, jitterMax, Nc, Nll, Tpll, Pll, BWres, ETH, ENC)

        


if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Pasar los parámetros
    windows = MainWindows()
    windows.show()
    app.exec_()