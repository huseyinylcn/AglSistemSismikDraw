from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from tkinter import *
from main import *
from data import * 
 
fig2, fax = plt.subplots(1,1,figsize=(21, 4.9))
fig3, fax3 = plt.subplots(1,1,figsize=(21, 4.9))
fig4, fax4 = plt.subplots(1,1,figsize=(21, 4.9))

detailSetData, = fax.plot(uzun_dizi, linewidth=1.5, color="green")
fax.set_facecolor('k')
fig2.patch.set_facecolor('black')
fig2.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, hspace=0)


fax.set_title("E-W",color="green",fontsize=20)
fax3.set_title("G-K",color="blue",fontsize=20)
fax4.set_title("Z",color="red",fontsize=20)



fax.spines['bottom'].set_color('white') 
fax.spines['left'].set_color('white') 
fax.spines['top'].set_color('none')  
fax.spines['right'].set_color('none')  

fax.tick_params(axis='x', colors='white') 
fax.tick_params(axis='y', colors='white')  






detailSetData2, = fax3.plot(uzun_dizi2, linewidth=1.5, color="blue")
fax3.set_facecolor('k')
fig3.patch.set_facecolor('black')
fig3.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, hspace=0)




fax3.spines['bottom'].set_color('white') 
fax3.spines['left'].set_color('white') 
fax3.spines['top'].set_color('none')  
fax3.spines['right'].set_color('none')  

fax3.tick_params(axis='x', colors='white') 
fax3.tick_params(axis='y', colors='white')  

detailSetData3, = fax4.plot(uzun_dizi3, linewidth=1.5, color="red")
fax4.set_facecolor('k')
fig4.patch.set_facecolor('black')
fig4.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, hspace=0)




fax4.spines['bottom'].set_color('white') 
fax4.spines['left'].set_color('white') 
fax4.spines['top'].set_color('none')  
fax4.spines['right'].set_color('none')  

fax4.tick_params(axis='x', colors='white') 
fax4.tick_params(axis='y', colors='white')





detailFrame = Frame(root, bg="green")
detailFrame2 = Frame(root, bg="green")
detailFrame3 = Frame(root, bg="green")

canvas1 = FigureCanvasTkAgg(fig2, master=detailFrame)
canvas1.get_tk_widget().pack()

canvas2 = FigureCanvasTkAgg(fig3, master=detailFrame2)
canvas2.get_tk_widget().pack()

canvas3 = FigureCanvasTkAgg(fig4, master=detailFrame3)
canvas3.get_tk_widget().pack()



    
  
