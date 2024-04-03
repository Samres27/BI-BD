from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
website="https://tarifas.att.gob.bo/index.php/tarifaspizarra/tarifasInternetFijo"


    
    
driver = webdriver.Firefox()   ##verificar la version que firefox, tambien puede ser chrome 
driver.get(website)
time.sleep(1)

all_maches=driver.find_element(By.CLASS_NAME,"dataTables_length")
selecionar=all_maches.find_element(By.XPATH,"//select/option[@value='-1']").click()
time.sleep(1)
df=pd.DataFrame()
table=driver.find_element(By.CLASS_NAME,"row")
tablehead=table.find_elements(By.CLASS_NAME,"text-center")
i=0
ls1=[]
ls2=[]
ls3=[]
ls4=[]
ls5=[]
ls6=[]
for x in tablehead:
    i+=1
    if i>6:
        i2=i%7
        texto=x.text
        match i2:
            
            case 0: print(str(i),)
            case 1: ls1.append(texto)
            case 2: ls2.append(texto)
            case 3: ls3.append(texto)
            case 4: ls4.append(texto)
            case 5: ls5.append(texto)
            case 6: ls6.append(texto)

    
    

driver.quit()
df=pd.DataFrame()
df["OPERADOR"]=ls1
df["DEPARTAMENTO"]=ls2
df["NOMBRE TARIFA"]=ls3
df["VELOCIDAD DE BAJADA(MBPS)"]=ls4
df["PRECIO (BS)"]=ls5
df["TIPO DE CONEXION"]=ls6
df.to_csv("tarifas.csv",index=False)
