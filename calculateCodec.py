#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:28:44 2021

@author: josel
"""
import math
import erlangB as erlangB
import pandas as pd


def calculateCodec(minimunMos, Rr, jitterMin, jitterMax, Nc, Nl, Tpll, Pll, BWres) :
    codecInfo = {
            "G711": {
                "CSS": 80, 
                "CSI": 10, 
                "MOS":4.1, 
                "VPS":160, 
                "VPSs":20, 
                "PPS":50,
                "BWmp":82.8,
                "BWcRTP":67.6,
                "BWeth":87.2
             },
             "G729":{
                "CSS": 10, 
                "CSI": 10, 
                "MOS":3.92, 
                "VPS":20, 
                "VPSs":20, 
                "PPS":50,
                "BWmp":26.8,
                "BWcRTP":11.6,
                "BWeth":31.2
             },
             "G723.1(6.3)":{
                "CSS": 24, 
                "CSI": 30, 
                "MOS":3.9, 
                "VPS":24, 
                "VPSs":30, 
                "PPS":33.3,
                "BWmp":18.9,
                "BWcRTP":8.8,
                "BWeth":21.9
             },
             "G723.1(5.3)":{
                "CSS": 20, 
                "CSI": 30, 
                "MOS":3.8, 
                "VPS":20, 
                "VPSs":30, 
                "PPS":33.3,
                "BWmp":17.9,
                "BWcRTP":7.7,
                "BWeth":20.8
             },
             "G726(32)":{
                "CSS": 20, 
                "CSI": 5, 
                "MOS":3.5, 
                "VPS":80, 
                "VPSs":20, 
                "PPS":50,
                "BWmp":50.8,
                "BWcRTP":35.6,
                "BWeth":55.2
             },
             "G728":{
                "CSS": 10, 
                "CSI": 5, 
                "MOS":3.61, 
                "VPS":60, 
                "VPSs":30, 
                "PPS":33.3,
                "BWmp":28.5,
                "BWcRTP":18.4,
                "BWeth":31.5
             },
             "G722_64k":{
                "CSS": 80, 
                "CSI": 10, 
                "MOS":4.13, 
                "VPS":160, 
                "VPSs":20, 
                "PPS":50,
                "BWmp":82.8,
                "BWcRTP":67.6,
                "BWeth":87.2
            }
    }
    
    Transporte_Red = {
        "RTP":12,
        "UDP":8,
        "IP":20
        }
    
    Enlace = {
        "ETHERNET":14,
        "ETHERNET8021Q":18,
        "ETHERNETQ":22,
        "PPP":6,
        "PPOE":20
        }
    
    Tuneles = {
        "IPSEC":50,
        "L2TP":24,
        "MPLS":4   
        }
    
    #IMPRIME TODOS LOS CODECS Y SUS VALORES
    #for id, info in codecInfo.items():
    #    print("\nCodec ID:", id)
    #    for key in info:
    #           print(key + ':', info[key])
                
                
    validCodec = []
    resultValues={}
    #BUSCA LOS CODECS VALIDOS DADO UN MOS
    for id, info in codecInfo.items():
        if info["MOS"] > minimunMos:
            validCodec.append(id) #Añadimos al vector cada uno de los codecs validos 
            #Para cada codec correcto creo un diccionario con los valores que tomará todo lo que calculemos
            resultValues.update(
               {id:{
                         "Rt":"",
                         "BHT":"",
                         "Nll":"",
                         "BWll":"",
                         "BWst":""
                      }  
                } 
             )
            
    print("\nVALID CODEC", validCodec)   
    print(resultValues)
    
    
    
    stringResults=[]
    
    #Get Delay from all valid codecs
    for i in validCodec:
       Ro=codecInfo[i]["VPSs"]+0.1*codecInfo[i]["CSI"]
       Rd=0.1*codecInfo[i]["CSI"]*codecInfo[i]["VPSs"]/codecInfo[i]["CSI"]
       RjitterMin=jitterMin*30
       RjitterMax=jitterMax*30
       minJitter=math.ceil(RjitterMin/codecInfo[i]["VPSs"])*codecInfo[i]["VPSs"]
       maxJitter=math.floor(RjitterMax/codecInfo[i]["VPSs"])*codecInfo[i]["VPSs"]
       Rt=Ro+Rr+Rd+minJitter
       print("Retardo total for CODEC "+  i + " :" + str(Rt))
       resultValues[i]["Rt"]=Rt
    

       BHT=Nc*Nl*Tpll/60
       print("Tráfico hora cargada (Erlangs)", BHT)
       resultValues[i]["BHT"]=BHT
    
       Nll=erlangB.lines(BHT,Pll)
       print("Number of calls ", Nll)
       resultValues[i]["Nll"]=Nll
       #CALCULO DEL ANCHO DE BANDA PARA RTP
       TRAMAS_VOZ = 4
       Lcabecera = Enlace["ETHERNET8021Q"] + Enlace["PPP"] + Transporte_Red["IP"] + Transporte_Red["UDP"] + Transporte_Red["RTP"] + TRAMAS_VOZ
       Lpaquete = (Lcabecera + codecInfo["G711"]["VPS"]) * 8
       BWLL = Lpaquete * codecInfo["G711"]["PPS"]
       BWst = 160 * BWLL * (1 + BWres)
       print("\nAncho de banda de llamada:", BWLL)
       print("Ancho de banda SIPTRUNK", BWst)
    
       #CALCULO DEL ANCHO DE BANDA PARA cRTP
       COMPRIMIDO = 4
       Lcabecera = Enlace["ETHERNET8021Q"] + Enlace["PPP"] + COMPRIMIDO + TRAMAS_VOZ
       Lpaquete = (Lcabecera + codecInfo["G711"]["VPS"]) * 8
       BWLL = Lpaquete * codecInfo["G711"]["PPS"]
       BWst = 160 * BWLL * (1 + BWres)
       print("\nAncho de banda de llamada comprimido:", BWLL)
       print("Ancho de banda SIPTRUNK comprimido", BWst)
    
       resultValues[i]["BWll"]=BWLL
       resultValues[i]["BWst"]=BWst
       stringResults.append([ i, codecInfo[i]["MOS"], (resultValues[i]["Rt"]), (resultValues[i]["BHT"]), (resultValues[i]["Nll"]), (resultValues[i]["BWll"]), (resultValues[i]["BWst"]) ]) 
    
    stringTable = pd.DataFrame(stringResults, columns = ['CODEC','MOS', "RT", "BHT", "Nll", "BWll", "BWst"])
    print(stringTable)

def main():
    calculateCodec(4,75,1.5,2,150,20,3, 0.03, 0.1)

if __name__ == '__main__':
    main()