from tkinter import *

from main import *




screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
def tcpSetting(): 
    
    port = entry.get()
    with open("port.txt", "w") as file:
        file.write(port)
    
    
    ipadres = ipentry.get()
    with open("ipadres.txt", "w") as file:
        file.write(ipadres)
    
    writee()
    
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

portbtn = Button(setting,text="KAYDET", command=tcpSetting)
portbtn.grid(row=2,column=0)
writee()
print(portFile)