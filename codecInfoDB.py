#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:28:44 2021
@author: josel
"""
import math
import erlangB as erlangB
import pandas as pd

#Esta clase contiene todos los códecs, tamaño de los túneles, protocolos y
#tamaño de tramas de voz. Están guardadaos en un diccionario para poder usarlo
#en la clase calculateCodec
class codecInfoClass:
   codecList = {
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
        "ETHERNETQinQ":22,
        "PPP":6,
        "PPOE":20
   }
   Tuneles = {
        "IPSEC":50,
        "L2TP":24,
        "MPLS":4   
   } 
   TRAMAS_VOZ = 4


   



