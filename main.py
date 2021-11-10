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
         }
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
