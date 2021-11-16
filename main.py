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

        #self.lPruebas.setText("Aquí con mis cosas")
        self.pbCalcular.setText("Siguiente paso")
        self.pbCalcular.clicked.connect(self.siguientePaso)

    def siguientePaso(self):
        Nc=self.iNC.value();
        Nl=self.iNC_2.value();
        Tpll=self.spinBox.value();
        Pll=self.doubleSpinBox.value();
        BWres=self.doubleSpinBox_2.value();
        #self.lPruebas.setText("Pos sa acabó")
        #self.tabWidget.setEnabled(1)
        #self.w = ResultsWindow()
        #self.w.show()
        #self.hide()
        calculateCodec.calculateCodec(4, 75, 1.5, 2, Nc, Nl, Tpll, Pll, BWres)
        

        
    pass


        


if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Pasar los parámetros
    windows = MainWindows()
    windows.show()
    app.exec_()