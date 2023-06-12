
import numpy as np
from tkinter import *
import time
import threading

from main import *
from setting import *
from ivmeGrafik import *
from detail import *
from data import *

def two():
   for widget in root.winfo_children():
       widget.pack_forget()
   setting.pack()
   start_Dgrafik1()
   buttonAll.pack()
  
def main():
   for widget in root.winfo_children():
       widget.pack_forget()
   box.pack(padx=5,pady=5)
   buttonAll.pack()
   start_grafik()

def detay1():
    for widget in root.winfo_children():
       widget.pack_forget()
    detailFrame.pack()
    buttonAll.pack()
    start_Dgrafik1()
    
    
def detay2():
    for widget in root.winfo_children():
       widget.pack_forget()
    detailFrame2.pack()
    buttonAll.pack()
    start_Dgrafik2()

def detay3():
    for widget in root.winfo_children():
       widget.pack_forget()
    detailFrame3.pack()
    buttonAll.pack()
    start_Dgrafik3() 
    


    


buttonAll = Frame(root, width=820,height=100,bg="black")
buttonAll.pack(padx=5,pady=5)
Button(buttonAll,text="Ayarlar",width=25,height=3,bg="orange",command=two).pack(side=RIGHT, padx=10,pady=5)
Button(buttonAll,text="Detay",width=25,height=3,bg="red").pack(side=RIGHT, padx=10,pady=5)
Button(buttonAll,text="Detay",width=25,height=3,bg="yellow").pack(side=RIGHT, padx=10,pady=5)
Button(buttonAll,text="Ana Sayfa",width=25,height=3,bg="tomato",command=main).pack(side=RIGHT, padx=10,pady=5)




Button(box,text="🍳",width=1,height=1,bg="white",command=detay1).place(x=770,y=10)
Button(box,text="🍳",width=1,height=1,bg="white",command=detay3).place(x=770,y=350)
Button(box,text="🍳",width=1,height=1,bg="white",command=detay2).place(x=770,y=200)


Button(detailFrame,text="⚽",width=2,height=1,bg="red",command=startbebek).place(x=770,y=10)
Button(detailFrame2,text="⚽",width=2,height=1,bg="red",command=startbebek2).place(x=770,y=10)
Button(detailFrame3,text="⚽",width=2,height=1,bg="red",command=startbebek3).place(x=770,y=10)


def data():
    while True:
        yeni_eleman = np.random.rand()
        uzun_dizi.append(yeni_eleman)
        del uzun_dizi[0] 
        uzun_dizi2.append(yeni_eleman)
        del uzun_dizi2[0] 
        uzun_dizi3.append(yeni_eleman)
        del uzun_dizi3[0] 
      
        time.sleep(0.01)
       
data_thread = threading.Thread(target=data)
data_thread.start()
   
   
root.mainloop() 






