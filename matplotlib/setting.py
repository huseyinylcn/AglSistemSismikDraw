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
    



















setting = Frame(root,bg="white", width=800, height=500)


labelFrm = Frame(setting,bg="white",padx=5)
labelFrm.grid(row=0, column=0, columnspan=8,sticky="w")

portLabe = Label(labelFrm,text="NOT: İvme ölçeri Aktifleştir ve eşik değerini belirle belirlenen değeri gecerse o zaman aralığındaki veriyi sunucuya  kaydet ",bg="white", anchor="w",font=("Arial",11))
portLabe.pack(side="left")



labelFrme = Frame(setting,bg="white",padx=5)
labelFrme.grid(row=1,column=0,sticky="w")

portLabel = Label(labelFrme,text="PORT: ",bg="white", anchor="w")
portLabel.pack(side="left")

btnFrme = Frame(setting,bg="white",padx=5,pady=2)
btnFrme.grid(row=2,column=0,sticky="w")

entry = Entry(btnFrme,width=17,font=("Arial",14),fg="black")
entry.pack()












ipFrme = Frame(setting,bg="white",padx=27,pady=2)
ipFrme.grid(row=1,column=1,sticky="w")

ipLabel = Label(ipFrme,text="İP ADRESİ: ",bg="white")
ipLabel.pack()

ipeFrme = Frame(setting,bg="white",padx=5,pady=2)
ipeFrme.grid(row=2,column=1,sticky="w")

ipentry = Entry(ipeFrme,width=17,font=("Arial",14),fg="black")
ipentry.pack()







esikLabelFrame = Frame(setting,bg="white",padx=27,pady=2)
esikLabelFrame.grid(row=1,column=2,sticky="w")

esikLabel = Label(esikLabelFrame,text="EŞİK DEĞERİ (G): ",bg="white")
esikLabel.pack()

esikeFrme = Frame(setting,bg="white",padx=5,pady=2)
esikeFrme.grid(row=2,column=2,sticky="w")

esikentry = Entry(esikeFrme,width=17,font=("Arial",14),fg="black")
esikentry.pack()
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

labelFr = Frame(setting,bg="white",padx=5)
labelFr.grid(row=3, column=0, columnspan=8,sticky="w")

portLab = Label(labelFr,text="Sismometre",bg="white", anchor="w",font=("Arial",11))
portLab.pack(side="left")



labelFrme2 = Frame(setting,bg="white",padx=5)
labelFrme2.grid(row=4,column=0,sticky="w")

portLabel2 = Label(labelFrme2,text="PORT: ",bg="white", anchor="w")
portLabel2.pack(side="left")

btnFrme2 = Frame(setting,bg="white",padx=5,pady=2)
btnFrme2.grid(row=5,column=0,sticky="w")

entry2 = Entry(btnFrme2,width=17,font=("Arial",14),fg="black")
entry2.pack()












ipFrme2 = Frame(setting,bg="white",padx=27,pady=2)
ipFrme2.grid(row=4,column=1,sticky="w")

ipLabel2 = Label(ipFrme2,text="İP ADRESİ: ",bg="white")
ipLabel2.pack()

ipeFrme2 = Frame(setting,bg="white",padx=5,pady=2)
ipeFrme2.grid(row=5,column=1,sticky="w")

ipentry2 = Entry(ipeFrme2,width=17,font=("Arial",14),fg="black")
ipentry2.pack()







esikLabelFrame2 = Frame(setting,bg="white",padx=27,pady=2)
esikLabelFrame2.grid(row=4,column=2,sticky="w")

esikLabel2 = Label(esikLabelFrame2,text="EŞİK DEĞERİ (G): ",bg="white")
esikLabel2.pack()

esikeFrme2 = Frame(setting,bg="white",padx=5,pady=2)
esikeFrme2.grid(row=5,column=2,sticky="w")

esikentry2 = Entry(esikeFrme2,width=17,font=("Arial",14),fg="black")
esikentry2.pack()



uzat3 = Label(setting,text=".")
uzat3.grid(row=6,column=0)

uzat4 = Label(setting,text=".")
uzat4.grid(row=7,column=0)

uzat5 = Label(setting,text=".")
uzat5.grid(row=8,column=0)

uzat6 = Label(setting,text=".")
uzat6.grid(row=9,column=0)

uzat7 = Label(setting,text=".")
uzat7.grid(row=10,column=0)

uzat8 = Label(setting,text=".")
uzat8.grid(row=11,column=0)

uzat9 = Label(setting,text=".")
uzat9.grid(row=12,column=0)
writee()








