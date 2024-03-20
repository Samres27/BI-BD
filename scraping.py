import requests
from bs4 import BeautifulSoup
import sqlite3
con = sqlite3.connect("datos.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS datos (titulo VARCHAR(55), fecha_publicacion VARCHAR(25), cuerpo VARCHAR(500), precio VARCHAR(25),descripcion VARCHAR(555));")

page="https://clasificados.lostiempos.com/inmuebles"

text=requests.get(page)
#print(text.text)
htmlContent=BeautifulSoup(text.text,features="html.parser")
listaCont=htmlContent.find_all("div",class_="views-row")


for x in listaCont:
    sql="""insert into datos (titulo, fecha_publicacion, cuerpo, precio,descripcion) values (?, ?, ?, ?, ?);"""
    datosintro=(str(x.find('div',class_="title").get_text().replace("\n","")),x.find('div',class_="publish-date").get_text().replace("\n",""),
                x.find('div',class_="body").get_text().replace("\n",""),x.find('div',class_="ads-price").get_text().replace("\n","")
                ,x.find('div',class_="description").get_text().replace("\n",""))
    
    cur.execute(sql,datosintro)
    

con.commit() 
con.close()