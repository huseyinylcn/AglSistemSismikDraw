
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
   grafik_false()
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
    


onlineIf = False
def data():
    while onlineIf:
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



 


    
def tcpSetting(): 
    global check_var, onlineIf
    port = entry.get()
    with open("port.txt", "w") as fil:
        fil.write(port)

    ipadres = ipentry.get()
    with open("ipadres.txt", "w") as file:
        file.write(ipadres)
    if check_var.get() == 1:
        with open("kontrol.txt","w") as warning:
            warning.write("true")
        print(check_var.get())
    if check_var.get() == 0:
        with open("kontrol.txt","w") as warnin:
            warnin.write("false")
        print(check_var.get())
    
    with open("kontrol.txt","r") as koplot:
        okunanaDeger = koplot.read()
    if okunanaDeger == "true":
        onlineIf = True
        data_thread = threading.Thread(target=data)
        data_thread.start()
        
    else:
        onlineIf = False
    
    
    
    writee()
 
   

def startFunch(): 
    global onlineIf, check_var,data_thread
    with open("kontrol.txt","r") as file:
        start = file.read()
    if start == "true":
        onlineIf = True
        data_thread = threading.Thread(target=data)
        data_thread.start()
        start_grafik()
        check_var = IntVar(value=1)     
    else:
        onlineIf = False
        check_var = IntVar(value=0)       
startFunch()


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

tcpLoginBtn = Frame(setting,bg="white",padx=10,pady=5)
tcpLoginBtn.grid(row=2,column=4,sticky="w")

portbtn = Button(tcpLoginBtn,text="KAYDET",width=13, command=tcpSetting)
portbtn.pack()

radio_var = IntVar()
tcpLoginBt = Frame(setting,bg="white",padx=10,pady=5)
tcpLoginBt.grid(row=2,column=3,sticky="w")

check_button = Checkbutton(tcpLoginBt, text="AKTİF", variable=check_var,bg="white",font=("Arial",12))
check_button.pack()

# ???????????????????
tcpLoginBtn2 = Frame(setting,bg="white",padx=10,pady=5)
tcpLoginBtn2.grid(row=5,column=4,sticky="w")

portbtn2 = Button(tcpLoginBtn2,text="KAYDET",width=13, )
portbtn2.pack()


tcpLoginBt2 = Frame(setting,bg="white",padx=10,pady=5)
tcpLoginBt2.grid(row=5,column=3,sticky="w")

check_button2 = Checkbutton(tcpLoginBt2, text="AKTİF",bg="white",font=("Arial",12))
check_button2.pack()







root.mainloop() 






