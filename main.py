#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:28:44 2021

@author: josel
"""
import math
import erlangB as erlangB

codecInfo1 = {
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
            "VPSb":30, 
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
            "VPSb":30, 
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
            "VPSb":20, 
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
            "VPSb":30, 
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
            "VPSb":20, 
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
for id, info in codecInfo1.items():
    print("\nCodec ID:", id)
    for key in info:
            print(key + ':', info[key])
            
            
validCodec = []
#BUSCA LOS CODECS VALIDOS DADO UN MOS
for id, info in codecInfo1.items():
    if info["MOS"] > 4:
        validCodec.append(id)    
        
print("\nVALID CODEC", validCodec)   

Ro=codecInfo1["G711"]["VPSs"]+0.1*codecInfo1["G711"]["CSI"]
Rr=75;
Rd=0.1*codecInfo1["G711"]["CSI"]*codecInfo1["G711"]["VPSs"]/codecInfo1["G711"]["CSI"]

RjitterMin=1.5*30
RjitterMax=2*30
minJitter=math.ceil(RjitterMin/codecInfo1["G711"]["VPSs"])*codecInfo1["G711"]["VPSs"]
maxJitter=math.floor(RjitterMax/codecInfo1["G711"]["VPSs"])*codecInfo1["G711"]["VPSs"]


Rt=Ro+Rr+Rd+minJitter

print("Retardo total", Rt)

Nc=150
Nl=20
Tpll=3
BHT=Nc*Nl*Tpll/60
print("Tráfico hora cargada (Erlangs)", Rt)


Nll=erlangB.lines(BHT,0.03)
print("Number of calls ", Nll)

#CALCULO DEL ANCHO DE BANDA PARA RTP
TRAMAS_VOZ = 4
BWres = 0.1 #Esto se llama en la funcion
Lcabecera = Enlace["ETHERNET8021Q"] + Enlace["PPP"] + Transporte_Red["IP"] + Transporte_Red["UDP"] + Transporte_Red["RTP"] + TRAMAS_VOZ
Lpaquete = (Lcabecera + codecInfo1["G711"]["VPS"]) * 8
BWLL = Lpaquete * codecInfo1["G711"]["PPS"]
BWst = 160 * BWLL * (1 + BWres)
print("\nAncho de banda de llamada:", BWLL)
print("Ancho de banda SIPTRUNK", BWst)

#CALCULO DEL ANCHO DE BANDA PARA RTP
COMPRIMIDO = 4
Lcabecera = Enlace["ETHERNET8021Q"] + Enlace["PPP"] + COMPRIMIDO + TRAMAS_VOZ
Lpaquete = (Lcabecera + codecInfo1["G711"]["VPS"]) * 8
BWLL = Lpaquete * codecInfo1["G711"]["PPS"]
BWst = 160 * BWLL * (1 + BWres)
print("\nAncho de banda de llamada comprimido:", BWLL)
print("Ancho de banda SIPTRUNK comprimido", BWst)



