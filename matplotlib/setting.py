from tkinter import *

from main import *




screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

    
portFile = ''
ipadresFile = ''

def writee():
    global portFile,ipadresFile
    with open("port.txt", "r") as file:
        portFile =  file.read()
    with open("ipadres.txt", "r") as file:
        ipadresFile =  file.read()
    
    entry.delete(0, END)  
    entry.insert(0, portFile)
    ipentry.delete(0, END)  
    ipentry.insert(0, ipadresFile)
    



setting = Frame(root,bg="white", width=screen_width, height=500)

portLabel = Label(setting,text="TCP İLE VERİ GÖNDERİLECEKSE PORT : ")
portLabel.grid(row=0,column=0)

entry = Entry(setting,width=40)

entry.grid(row=0, column=1,)



ipLabel = Label(setting,text="TCP İLE VERİ GÖNDERİLECEKSE İP ADRESİ : ")
ipLabel.grid(row=1,column=0)

ipentry = Entry(setting,width=40)
ipentry.grid(row=1, column=1,)


writee()

onlilabel = Label(setting,text="adxl345 veri okuma aktifleştir: ")
onlilabel.grid(row=3,column=0)

onliinput = Entry(setting,width=40)
onliinput.grid(row=3, column=1,)


