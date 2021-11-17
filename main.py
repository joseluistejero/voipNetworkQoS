from PyQt5 import QtWidgets
from main_ui import *
from ventana_ui import *
import calculateCodec

class ResultsWindow(QtWidgets.QMainWindow, Ui_VentanaWindow):

    def __init__(self, result, valuesIntroduced):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.valuesIntroduced=valuesIntroduced
        numberOfValidCodecs=len(result)
        if(numberOfValidCodecs>0):
            self.tableWidget.setRowCount(numberOfValidCodecs)
            self.validCodecs.setProperty("intValue", numberOfValidCodecs)
            for i in range(numberOfValidCodecs):
                for j in range(len(result[i])):
                    newitem = QtWidgets.QTableWidgetItem(str(result[i][j]))
                    self.tableWidget.setItem(i, j, newitem)
        else :
            self.pbCalcular.clicked.connect(self.recalculate)
    
    def recalculate(self):
        self.hide()
        self.w = MainWindows(bool(0),self.valuesIntroduced)
        self.w.show()
            
    


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, firstTry, values): 
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabMenu.setCurrentIndex(0)
        self.pbCalcular.clicked.connect(self.goToSecondPage)
        if(not firstTry):
            self.Nc.setValue(values[0]);
            self.Nll.setValue(values[1]);
            self.Tpll.setValue(values[2]);
            self.Pb.setValue(values[3]);
            self.ETH.setCurrentText(values[4]);
            self.ENC.setCurrentText(values[5]);
            self.TUN.setCurrentText(values[6]);
            self.BWres.setValue(values[7]);
            self.Rr.setValue(values[8]);
            self.minJitter.setValue(values[9]);
            self.maxJitter.setValue(values[10]);
            self.MOS.setCurrentText(values[11]);

    def goToSecondPage(self):
        self.tabMenu.setCurrentIndex(1)
        self.progressBar.setValue(25)
        self.pbCalcular.clicked.connect(self.goToThirdPage)
        
    def goToThirdPage(self):
        self.tabMenu.setCurrentIndex(2)
        self.progressBar.setValue(50)
        self.pbCalcular.clicked.connect(self.goToFourthPage)   
        
    def goToFourthPage(self):
        self.tabMenu.setCurrentIndex(3)
        self.progressBar.setValue(75)
        self.pbCalcular.clicked.connect(self.goToFifthPage)   
    def goToFifthPage(self):
        self.tabMenu.setCurrentIndex(4)
        self.progressBar.setValue(75)
        self.pbCalcular.setText("Calcular")
        self.pbCalcular.clicked.connect(self.calcular)        

    def calcular(self):
        Nc=self.Nc.value();
        Nll=self.Nll.value();
        Tpll=self.Tpll.value();
        Pb=self.Pb.value();
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
    
        valuesIntroduced=[Nc,Nll,Tpll,Pb,ETH,ENC,TUN,BWres,Rr,jitterMin,jitterMax,mosString]
        stringTable=calculateCodec.calculateCodec(mos, Rr, jitterMin, jitterMax, Nc, Nll, Tpll, Pb, BWres, ETH, ENC, TcWan, Rt)
        self.w = ResultsWindow(stringTable,valuesIntroduced)
        self.w.show()
        self.hide()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Pasar los parámetros
    windows = MainWindows(bool(1),[])
    windows.show()
    app.exec_()