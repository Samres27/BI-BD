import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
tr='''schtasks /Create /SC DAILY /mo {repDia} /TN PythonExtracionClas /TR "'{pathPython}' '{pathScript}'"'''
pathScrp=os.getcwd()+"/scrapingClasificados.py"

    

ventana=tk.Tk()
ventana.title("configuracion")
ventana.geometry("500x300")

labelDesc=tk.Label(ventana,text="Configura los dias para Extracion",font=("Arial", 18),height=2, anchor="center")
labelDesc.pack()

labelDefDias=tk.Label(ventana,text="Cada cuantos dias:",font=("Arial", 12),height=2, anchor="e")
entryDias=tk.Entry(ventana,font=("Arial",14),justify="center")
labelDefDias.place(x=50,y=60)
entryDias.place(x=220,y=70,width=50)

labelDefPathPy=tk.Label(ventana,text="Path de python:",font=("Arial", 12),height=2, anchor="e")
entryPathPy=tk.Entry(ventana,font=("Arial",12),justify="center")
labelDefPathPy.place(x=50,y=100)
entryPathPy.place(x=180,y=110,width=250)
arc=""
def extraerArc():
    arc=filedialog.askopenfilename(initialdir="C:/",title="seleciona el ejecutable python.exe",filetypes=[("exe file",".exe")])
    
    entryPathPy.insert(0,str(arc))
    
buttonSelec=tk.Button(ventana,text="select",command=extraerArc)
buttonSelec.place(x=440,y=110,width=50)

def checkAndSave():
    var1=entryDias.get()
    var2=entryPathPy.get()
    if not(os.path.exists(var2)) or not(var1.isdigit()):
        messagebox.showerror(message="revise sus campos",title="Error")
    else:
        cd=tr.format(repDia=var1 ,pathPython=var2, pathScript=pathScrp)
        print(cd)
        os.system(cd)
        ventana.quit()

buttonOk=tk.Button(ventana,text="Listo",font=("Arial", 12),command=checkAndSave)

buttonOk.place(x=150,y=180,width=200)


ventana.mainloop()

