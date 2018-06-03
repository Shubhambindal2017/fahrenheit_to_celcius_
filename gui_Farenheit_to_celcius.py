from Tkinter import *
from tkMessageBox import *

class Converter(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.pack( expand=YES , fill=BOTH)
        self.master.title("FARENHIET TO CELCIUS CONVERTER")
        self.master.geometry("500x100")

        self.frame1=Frame(self)
        self.frame1.pack()
        
        self.text=Entry(self.frame1,width=50)
        self.text.insert(INSERT,"ENTER TEMPERATURE IN FARENHEIT")
        self.text.bind("<Return>",self.converter)
        self.text.pack(side=LEFT )

    def converter(self,event):

        fahrenheit=event.widget.get()
        fahrenheit1=float(fahrenheit)
        celcius=(float(5)/9)*(fahrenheit1 - 32 )
        celcius1=str(celcius)
        showinfo("MESSAGE", fahrenheit + " DEG. FAHRENHEIT IS CONVERTED INTO " + celcius1 + " DEG. CELCIUS")

Converter().mainloop()
# -*- coding: cp1252 -*-
