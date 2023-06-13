from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import *

from main import *
from data import *
from detail import *
    




fig,(ax1,ax2,ax3) = plt.subplots(3,1,figsize=(12, 4.9))
line, = ax1.plot(uzun_dizi, linewidth=0.5, color="green")

ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_facecolor('k')
ax1.set_ylabel('E - W', color='green', labelpad=-16,fontsize=15)


line2, = ax2.plot(uzun_dizi2, linewidth=0.5, color="blue")
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_facecolor('k')
ax2.set_ylabel('G - K', color='blue', labelpad=-16,fontsize=15)


line3, = ax3.plot(uzun_dizi3, linewidth=0.5, color="red")
ax3.set_xticks([])
ax3.set_yticks([])
ax3.set_facecolor('k')
ax3.set_ylabel('D - Y', color='red', labelpad=-16,fontsize=15)

fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0)

box = Frame(root, bg="green")
box.pack(padx=5,pady=5)

canvas = FigureCanvasTkAgg(fig, master=box)
canvas.get_tk_widget().pack()





grafik_flag = False
Dgrafik1_flag = False
Dgrafik2_flag = False
Dgrafik3_flag = False
def grafik():
    global grafik_flag
    line.set_data(range(len(uzun_dizi)), uzun_dizi) 
    line2.set_data(range(len(uzun_dizi2)), uzun_dizi2) 
    line3.set_data(range(len(uzun_dizi3)), uzun_dizi3)
    detailSetData.set_data(range(len(uzun_dizi)), uzun_dizi)
    detailSetData2.set_data(range(len(uzun_dizi2)), uzun_dizi2)
    detailSetData3.set_data(range(len(uzun_dizi3)), uzun_dizi3)
    fig.canvas.draw()
 
    ax1.set_ylim(-1,10)
    ax2.set_ylim(-1,10)
    ax3.set_ylim(-1,10)
    if grafik_flag:
        box.after(10, grafik)

def Dgrafik1():
    global Dgrafik1_flag
    detailSetData.set_data(range(len(uzun_dizi)), uzun_dizi)
    fig2.canvas.draw()
    fax.set_ylim(-0.5,1.5)
    if Dgrafik1_flag:
        detailFrame.after(10, Dgrafik1)

def Dgrafik2():
    global Dgrafik2_flag
    detailSetData2.set_data(range(len(uzun_dizi2)), uzun_dizi2)
    fig3.canvas.draw()
    fax3.set_ylim(-0.5,1.5)
    if Dgrafik2_flag:
        detailFrame2.after(10, Dgrafik2)

def Dgrafik3():
    global Dgrafik3_flag
    detailSetData3.set_data(range(len(uzun_dizi3)), uzun_dizi3)
    fig4.canvas.draw()
    fax4.set_ylim(-0.5,1.5)
    if Dgrafik3_flag:
        detailFrame3.after(10, Dgrafik3)

def start_grafik():
    global grafik_flag, Dgrafik1_flag, Dgrafik2_flag, Dgrafik3_flag
    if grafik_flag == False:
         grafik_flag = True
         Dgrafik1_flag = False
         Dgrafik2_flag = False
         Dgrafik3_flag = False
         grafik()

def start_Dgrafik1():
    global grafik_flag, Dgrafik1_flag, Dgrafik2_flag, Dgrafik3_flag
    grafik_flag = False
    Dgrafik1_flag = True
    Dgrafik2_flag = False
    Dgrafik3_flag = False
    Dgrafik1()

def start_Dgrafik2():
    global grafik_flag, Dgrafik1_flag, Dgrafik2_flag, Dgrafik3_flag
    grafik_flag = False
    Dgrafik1_flag = False
    Dgrafik2_flag = True
    Dgrafik3_flag = False
    Dgrafik2()

def start_Dgrafik3():
    global grafik_flag, Dgrafik1_flag, Dgrafik2_flag, Dgrafik3_flag
    grafik_flag = False
    Dgrafik1_flag = False
    Dgrafik2_flag = False
    Dgrafik3_flag = True
    Dgrafik3()

def startbebek():
    global grafik_flag, Dgrafik1_flag, Dgrafik2_flag, Dgrafik3_flag
    
    if Dgrafik1_flag == True:
        grafik_flag = False
        Dgrafik1_flag = False
        Dgrafik2_flag = False
        Dgrafik3_flag = False
        
    else:
        grafik_flag = False
        Dgrafik1_flag = True
        Dgrafik2_flag = False
        Dgrafik3_flag = False
    Dgrafik1()
        
    
def startbebek2():
    global grafik_flag, Dgrafik1_flag, Dgrafik2_flag, Dgrafik3_flag
    
    if Dgrafik2_flag == True:
        grafik_flag = False
        Dgrafik1_flag = False
        Dgrafik2_flag = False
        Dgrafik3_flag = False
        cursor = Cursor(fax, useblit=True, color='red', linewidth=1)
    else:
        grafik_flag = False
        Dgrafik1_flag = False
        Dgrafik2_flag = True
        Dgrafik3_flag = False
    Dgrafik2()
    
def startbebek3():
    global grafik_flag, Dgrafik1_flag, Dgrafik2_flag, Dgrafik3_flag
    
    if Dgrafik3_flag == True:
        grafik_flag = False
        Dgrafik1_flag = False
        Dgrafik2_flag = False
        Dgrafik3_flag = False
        cursor = Cursor(fax, useblit=True, color='red', linewidth=1)
    else:
        grafik_flag = False
        Dgrafik1_flag = False
        Dgrafik2_flag = False
        Dgrafik3_flag = True
    Dgrafik3()
         
def grafik_false():
    global grafik_flag, Dgrafik1_flag, Dgrafik2_flag, Dgrafik3_flag
    grafik_flag = False
    Dgrafik1_flag = False
    Dgrafik2_flag = False
    Dgrafik3_flag = False
    
