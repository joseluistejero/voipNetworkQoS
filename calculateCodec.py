#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:28:44 2021
@author: josel
"""
import math

from numpy import string_
import erlangB as erlangB
import pandas as pd
import codecInfoDB

class voipCodecs:
   
   def __init__(self):
      self.validCodec = []
      self.resultValues={}
      self.stringResults=[]
      self.allCodecs=codecInfoDB.codecInfoClass()
      self.codecInfo=self.allCodecs.codecList
      self.Transporte_Red=self.allCodecs.Transporte_Red
      self.Enlace=self.allCodecs.Enlace
      self.Tuneles=self.allCodecs.Tuneles
      self.TRAMAS_VOZ=self.allCodecs.TRAMAS_VOZ

   def getValidCodec(self):
      for id, info in self.codecInfo.items():
         if info["MOS"] > self.minimunMos:
            self.validCodec.append(id) #Añadimos al vector cada uno de los codecs validos 
            #Para cada codec correcto creo un diccionario con los valores que tomará todo lo que calculemos
            self.resultValues.update(
               {id:{
                         "Rt":"",
                         "BHT":"",
                         "Nll":"",
                         "BWll":"",
                         "BWst":"",
                         "NpaquetesRTP":"",
                         "Pperd":"",
                         "E":""
                      }  
                } 
             )
            
      print("\nVALID CODEC", self.validCodec)   
      print(self.resultValues)

   def getRetardoTotal(self):
      for i in self.validCodec:
       Ro=self.codecInfo[i]["VPSs"]+0.1*self.codecInfo[i]["CSI"]
       Rd=0.1*self.codecInfo[i]["CSI"]*self.codecInfo[i]["VPSs"]/self.codecInfo[i]["CSI"]
       jitterMax=2
       jitterMin=1.5
       RjitterMin=jitterMin*30
       RjitterMax=jitterMax*30
       minJitter=math.ceil(RjitterMin/self.codecInfo[i]["VPSs"])*self.codecInfo[i]["VPSs"]
       maxJitter=math.floor(RjitterMax/self.codecInfo[i]["VPSs"])*self.codecInfo[i]["VPSs"]
       Rtc=Ro+self.Rr+Rd
       Npaquetes=int((self.Rto-Rtc)/20)
       self.resultValues[i]["NpaquetesRTP"]=Npaquetes
       Rt=Ro+self.Rr+Rd+minJitter
       print("Retardo total for CODEC "+  i + " :" + str(Rt))
       self.resultValues[i]["Rt"]=Rt  
       

   def getBHT(self):
      for i in self.validCodec:
        self.BHT=self.Nc*self.Nl*self.Tpll/60.0
        print("Tráfico hora cargada (Erlangs)", self.BHT)
        self.resultValues[i]["BHT"]=self.BHT

   def getNumberOfCalls(self):
      for i in self.validCodec:
        Nll=erlangB.lines(self.resultValues[i]["BHT"],self.Pb)
        print("Number of calls ", Nll)
        self.resultValues[i]["Nll"]=Nll

   def getBWst(self):
      for i in self.validCodec:
         if (self.TcWan == "RTP") :
            Lcabecera = self.Enlace[self.ETH] + self.Enlace[self.ENC] + self.Transporte_Red["IP"] + self.Transporte_Red["UDP"] + self.Transporte_Red["RTP"] + self.TRAMAS_VOZ
            Lpaquete = (Lcabecera + self.codecInfo[i]["VPS"]) * 8
         else :
            COMPRIMIDO = 4
            Lcabecera = self.Enlace[self.ETH] + self.Enlace[self.ENC] + COMPRIMIDO + self.TRAMAS_VOZ
            Lpaquete = (Lcabecera + self.codecInfo[i]["VPS"]) * 8

         BWll = Lpaquete * self.codecInfo[i]["PPS"]
         BWst = self.resultValues[i]["Nll"] * BWll * (1 + self.BWres)
         print("\nAncho de banda de llamada comprimido:", BWll)
         print("Ancho de banda SIPTRUNK comprimido", BWst) 
         self.resultValues[i]["BWll"]=BWll
         self.resultValues[i]["BWst"]=BWst
      

   def toString(self):
        stringTable = pd.DataFrame(self.stringResults, columns = ['CODEC','MOS', "RT", "BHT", "Nll", "BWll", "BWst", "NPaquetesRTP", "Pperd", "E"])
        print(stringTable)
        return stringTable
   
   def calculateAll(self):
      self.validCodec = []
      self.resultValues={}
      self.stringResults=[]
      self.getValidCodec()
      self.getRetardoTotal()
      self.getBHT()
      self.getNumberOfCalls()
      self.getBWst()
      for i in self.validCodec:
         self.stringResults.append([ i, self.codecInfo[i]["MOS"], (self.resultValues[i]["Rt"]), (self.resultValues[i]["BHT"]), (self.resultValues[i]["Nll"]), (self.resultValues[i]["BWll"]), (self.resultValues[i]["BWst"]), (self.resultValues[i]["NpaquetesRTP"]), (self.Pperd), (self.E) ]) 
      return self.stringResults


def main():
    myCodec= voipCodecs()
    myCodec.minimunMos=4
    myCodec.Rr=75
    myCodec.Nc=150
    myCodec.Nl=20
    myCodec.Tpll=3
    myCodec.Rto=150
    myCodec.Pb=0.03
    myCodec.BWres=0.1
    myCodec.ETH="ETHERNET8021Q"
    myCodec.ENC="PPP"
    myCodec.TcWan="RTP"

    myCodec.calculateAll()

if __name__ == '__main__':
    main()
    

def getMosFromText(mosString):
        if (mosString=="Excelente"):
            mos=5
        elif (mosString=="Buena"):
            mos=4
        elif (mosString=="Aceptable"):
            mos=3
        elif (mosString=="Pobre"):
            mos=2
        else :
            mos=1
        return mos

def getRtoFromText(rtoString):
    if (rtoString=="Aceptable"):
            rto=150
    elif (rtoString=="Moderadamente aceptable"):
            rto=400
    return rto   
    
def getTextFromMos(mosValue):
    if (mosValue==5):
        mos="Excelente"
    elif (mosValue==4):
        mos="Buena"
    elif (mosValue==3):
        mos="Aceptable"
    elif (mosValue==2):
        mos="Pobre"
    else :
        mos="Mala"
    return mos   

def getProbabPaquete(p):
    q = (p[1]+p[2]*2+p[3]*3+p[4]*4+p[5]*5+p[6]*6+p[7]*7+p[8]*8+p[9]*9)/p[0]
    x = p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]+p[9]
    
    Pperd = x/(x+q)
    print(q)
    return Pperd

def getPromRafaga(p):
    q = (p[1]+p[2]*2+p[3]*3+p[4]*4+p[5]*5+p[6]*6+p[7]*7+p[8]*8+p[9]*9)/p[0]
    E = 1/q
    
    return E






