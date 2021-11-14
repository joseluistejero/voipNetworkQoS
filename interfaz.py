# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 19:10:37 2021

@author: HP
"""

from tkinter import * 
from tkinter import messagebox

window = Tk() 
window.title("Calculadora de red VoIP")
window.geometry('350x200')

lbl = Label(window, text="Introduzca el MOS requerido")
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)


def clicked():
    
     mos = txt.get()
     if mos >= "1" and mos <= "5":
          messagebox.showinfo('AVISO', 'Dato introducido correctamente')
          mos = int (mos)
     else: 
         messagebox.showerror('AVISO', 'Dato no válido')
         
    
btn = Button(window, text="OK", command=clicked)
btn.grid(column=2, row=0)



window.mainloop()