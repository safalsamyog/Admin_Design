from ttkbootstrap import Style
from tkinter import ttk
from tkinter import *
from ttkbootstrap.widgets import Meter
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
style=Style()
window=style.master
window.geometry('800x600')
window.config(bg='#efedf5')
window.title('Admin Pannel')
window.attributes('-alpha', 0.92)
icon=PhotoImage(file='s.png')
window.iconphoto(False,icon)
#=======================================chart===============================================
matplotlib.use("TkAgg")

# Create a figure of specific size
figure = Figure(figsize=(9.2, 2.7))

# Define the points for plotting the figure
plot = figure.add_subplot(1, 1, 1)
# Define Data points for x and y axis
x=np.linspace(1,1000,400)
plot.plot(np.cos(x), color="red")

# Add a canvas widget to associate the figure with canvas
canvas = FigureCanvasTkAgg(figure, window)
canvas.get_tk_widget().place(x=350,y=150*2.8)

#========================================frame==============================================
frame=Frame(window,bg='#180854').place(x=0,y=0,height=710,width=230)
frame2=Frame(window,bg='#180854').place(x=0,y=0,height=105,width=1400)
dash=Label(frame2,text='Dash Board',bg='#180854',fg='orange',font = "Verdana 26 bold").place(x=500,y=28)
photo1=PhotoImage(file='home1.png')
home=Label(frame,image=photo1,bg='#180854').place(x=10,y=120)
txt1=Button(frame,text='Home',bg='#180854',fg='white',font = "Verdana 13 bold").place(x=100,y=134)

#2nd
photo2=PhotoImage(file='mng.png')
manage=Label(frame,image=photo2,bg='#180854').place(x=10,y=120*2)
txt1=Button(frame,text='Manage',bg='#180854',fg='white',font = "Verdana 13 bold").place(x=100,y=134*2-15)

#3rd
photo3=PhotoImage(file='cc.png')
cc=Label(frame,image=photo3,bg='#180854').place(x=10,y=120*3)
txt1=Button(frame,text='Help',bg='#180854',fg='white',font = "Verdana 13 bold").place(x=100,y=134*3-25)

#4th
photo4=PhotoImage(file='s1.png')
abt=Label(frame,image=photo4,bg='#180854').place(x=10,y=120*4)
txt1=Button(frame,text='About Us',bg='#180854',fg='white',font = "Verdana 13 bold").place(x=100,y=134*3.9-25)

#5
photo5=PhotoImage(file='sq1.png')
sett=Button(frame,image=photo5,bg='#180854').place(x=1300,y=14)


#==================================================Another Frame=========================================
frame3=Frame(window,bg='#ffffff').place(x=350,y=140,height=250,width=920)
m1=Meter(metersize=180, padding=20, amountused=1200,amounttotal=2000, meterstyle='info.TLabel',labelstyle='danger.TLabel', labeltext='Total People').place(x=380,y=150)
m2=Meter(metersize=180, padding=20, amountused=100, meterstyle='danger.TMeter',labelstyle='info.TLabel', labeltext='Total Employe').place(x=380*2-100,y=150)
m3= Meter(metersize=180, padding=20, amountused=60, amounttotal=100, labelstyle='success.TLabel',labeltext='Profit Rate',meterstyle='primary.TMeter', stripethickness=10).place(x=320*3,y=150)

#=====================================================================
search=ttk.Entry(frame2,style='info.TEntry',background='white').place(x=900,y=36)
searhlabl=ttk.Label(frame2,text='Search',style='info.Inverse.TLabel',font=('Helvetica', 14,'bold')).place(x=1060,y=36,height=30,width=90)
#========================================Search=============================

if __name__=='__main__':
    window.mainloop()