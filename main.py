from PyQt5 import QtWidgets
from main_ui import *
from ventana_ui import *
import calculateCodec
import smtplib

#Esta clase la usaremos para crear la ventana donde saldrán los resultados calculados.
#Será una ventana emergente
class ResultsWindow(QtWidgets.QMainWindow, Ui_VentanaWindow):
    #Función para iniciar los atributos el objeto creado, también creamos la
    #tabla donde saldrán todos los códecs validos y sus características.
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
        self.sendMail.clicked.connect(self.enviarCorreo)
    #Función para volver a la página principal para modificar los valores introducidos
    def recalculate(self):
        self.hide()
        self.w = MainWindows(bool(0), self.myCodec)
        self.w.show()
         
    #Función que permite enviar un correo al administrador de la red con los 
    #resultados obtenidos
    def enviarCorreo(self):
        port=587 
        smtp_server = "correo.ugr.es" 
        sender_email = "joseluistejero@correo.ugr.es"
        receiver_email = "joseluistejero@correo.ugr.es"
        password=input (" Escribe la contraseña de tu correo ugr: ") 
        body=str(self.myCodec.toString())
        SUBJECT="Valid Codecs"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, body)
        with smtplib.SMTP(smtp_server, port) as server: 
          server.ehlo () # Puede omitirse 
          server.starttls () 
          server.ehlo () 
          server.login (sender_email, password) 
          server.sendmail (sender_email, receiver_email, message) 
          server.close () # Puede ser admitido

#Esta clase representa la página principal donde se introducen todos los datos
class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    #Función para iniciar los atributos el objeto creado. Permite cambiar los parámetros
    #al objeto para poder enseñarlo de nuevo en la ventana de resultados.
    def __init__(self, firstTry, myCodec): 
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabMenu.setCurrentIndex(0)
        self.pbCalcular.clicked.connect(self.goToSecondPage)
        if(not firstTry):
            self.Nc.setValue(myCodec.Nc)
            self.Nll.setValue(myCodec.Nl)
            self.Tpll.setValue(myCodec.Tpll)
            self.Pb.setValue(myCodec.Pb)
            self.ETH.setCurrentText(myCodec.ETH)
            self.ENC.setCurrentText(myCodec.ENC)
            self.TUN.setCurrentText(myCodec.TUN)
            self.BWres.setValue(myCodec.BWres)
            self.Rr.setValue(myCodec.Rr)
            self.MOS.setCurrentText(calculateCodec.getTextFromMos(myCodec.minimunMos))
            self.rutaFicheroLabel.setText(myCodec.rutaFichero)
            
    #Función para pasar a la segunda pestaña de la página principal
    def goToSecondPage(self):
        self.tabMenu.setCurrentIndex(1)
        self.progressBar.setValue(25)
        self.pbCalcular.clicked.connect(self.goToThirdPage)
    
    #Función para pasar a la tercera pestaña de la página principal        
    def goToThirdPage(self):
        self.tabMenu.setCurrentIndex(2)
        self.progressBar.setValue(50)
        self.pbCalcular.clicked.connect(self.goToFourthPage)   
    
    #Función para pasar a la cuarta pestaña de la página principal
    def goToFourthPage(self):
        self.tabMenu.setCurrentIndex(3)
        self.progressBar.setValue(75)
        self.pbCalcular.clicked.connect(self.goToFifthPage)   
        
    #Función para pasar a la quinta pestaña de la página principal
    def goToFifthPage(self):
        self.tabMenu.setCurrentIndex(4)
        self.progressBar.setValue(100)
        self.pbCalcular.setText("Calcular")
        self.pbCalcular.clicked.connect(self.calcular)      
        self.CargarFichero.clicked.connect(self.leerFichero) 
    
    #Función que permite seleccionar un fichero y guardar la ruta en una variable.
    def leerFichero(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        rutaFichero, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        self.rutaFicheroLabel.setText(rutaFichero)
        
    #Función para leer línea por línea un fichero y contar los grupos de 0 y 1 y 
    #guardarlos en un vector. Cada posición del vector refiere a la cantidad de 0 o de 1 juntos.
    #Ej: p[30,1,0,3,5] significaría que hay 30 ceros, 1 grupo con un solo 1, 3 grupos de 3 unos
    #y 5 grupos de 4 unos.
    def calcularRafagas(self):
        cont1 = 0
        p = [0,0,0,0,0,0,0,0,0,0]
        with open(self.rutaFicheroLabel.text()) as f:
            for linea in f:
                for a in linea:
                    if (a == "1"):
                        cont1+=1
                    elif (a == "0"):
                        p[cont1]+=1 
                        cont1=0
        p[0]+=p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]+p[9]
        return p
    
    
    #Esta función define los parámetros finales del objeto que enseñamos por pantalla
    #en la ventana de resultados
    def calcular(self):
        
        myCodec.Nc=self.Nc.value()
        myCodec.Nl=self.Nll.value()
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
        myCodec.Pperd=calculateCodec.getProbabPaquete(self.calcularRafagas())
        myCodec.E=calculateCodec.getPromRafaga(self.calcularRafagas())
        myCodec.rutaFichero=self.rutaFicheroLabel.text()
        
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

 