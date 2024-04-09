from bs4 import BeautifulSoup
import requests
import nums_from_string
import datetime
import pandas  as pd
pagina="https://clasificados.lostiempos.com/inmuebles?sort_by=created&sort_order=DESC&page="
np=0


titulo=[]
fechaPluc=[]
body=[]
precio=[]
descripcion=[]
while True:
    
    try:
        htmlP=requests.get(pagina+str(np)).text
        soup=BeautifulSoup(htmlP,features="html.parser")
        ts=soup.find_all("div",{"class":"views-row"})
    except:
        break
    np+=1
    for x in ts:
        
        titulo.append(x.find("div",{"class":"title"}).text.replace("\n",""))
        fechaPluc.append(x.find("div",{"class":"publish-date"}).text.replace("\n",""))
        
        cuerposs=x.find("div",{"class":"body"}).text.replace("\n","")
        body.append(cuerposs)
        preciov=x.find("div",{"class":"ads-price"}).text.replace("\n","").replace(" ","")
        if len(preciov)==0:
            s = nums_from_string.get_nums(cuerposs)
            precio.append(s[0])
        else: 
            precio.append(preciov)
        descripcion.append(x.find("div",{"class":"description"}).text.replace("\n",""))
        
datos=pd.DataFrame()
datos["titulo"]=titulo
datos["fecha de publicacion"]=fechaPluc
datos["body"]=body
datos["precio"]=precio
datos["descripcion"]=descripcion
dia=str(datetime.date.today())
datos.to_csv("datos"+dia+".csv")
