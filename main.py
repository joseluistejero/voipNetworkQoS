from PyQt5 import QtWidgets
from main_ui import *
from ventana_ui import *
import calculateCodec

class ResultsWindow(QtWidgets.QMainWindow, Ui_VentanaWindow):

    def __init__(self, result, myCodec ):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        numberOfValidCodecs=len(result)
        self.myCodec=myCodec
        if(numberOfValidCodecs>0):
            self.tableWidget.setRowCount(numberOfValidCodecs)
            self.validCodecs.setProperty("intValue", numberOfValidCodecs)
            for i in range(numberOfValidCodecs):
                for j in range(len(result[i])):
                    newitem = QtWidgets.QTableWidgetItem(str(result[i][j]))
                    self.tableWidget.setItem(i, j, newitem)

        self.pbCalcular.clicked.connect(self.recalculate)        

    
    def recalculate(self):
        self.hide()
        self.w = MainWindows(bool(0), self.myCodec)
        self.w.show()
            
    


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, firstTry, myCodec): 
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabMenu.setCurrentIndex(0)
        self.pbCalcular.clicked.connect(self.goToSecondPage)
        if(not firstTry):
            self.Nc.setValue(myCodec.Nc)
            self.Nll.setValue(myCodec.Nll)
            self.Tpll.setValue(myCodec.Tpll)
            self.Pb.setValue(myCodec.Pb)
            self.ETH.setCurrentText(myCodec.ETH)
            self.ENC.setCurrentText(myCodec.ENC)
            self.TUN.setCurrentText(myCodec.TUN)
            self.BWres.setValue(myCodec.BWres)
            self.Rr.setValue(myCodec.Rr)
            self.MOS.setCurrentText(calculateCodec.getTextFromMos(myCodec.minimunMos))

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
        self.progressBar.setValue(100)
        self.pbCalcular.setText("Calcular")
        self.pbCalcular.clicked.connect(self.calcular)        

    def calcular(self):

        myCodec.Nc=self.Nc.value()
        myCodec.Nll=self.Nll.value()
        myCodec.Tpll=self.Tpll.value()
        myCodec.Pb=self.Pb.value()
        myCodec.ETH=self.ETH.currentText()
        myCodec.ENC=self.ENC.currentText()
        myCodec.TUN=self.TUN.currentText()
        myCodec.BWres=self.BWres.value()
        myCodec.Rr=self.Rr.value()
        myCodec.TcWan=self.TcWan.currentText()
        myCodec.minimunMos=calculateCodec.getMosFromText(self.MOS.currentText())
        myCodec.Rto=calculateCodec.getRtoFromText(self.Rt.currentText())
        
        stringTable=myCodec.calculateAll()
        print(stringTable)
        self.w = ResultsWindow(stringTable,myCodec)
        self.w.show()
        self.hide()

    

if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Pasar los parámetros
    myCodec= calculateCodec.voipCodecs()
    windows = MainWindows(bool(1),myCodec)
    windows.show()
    app.exec_()

 