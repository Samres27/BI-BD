from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
website="https://www.zillow.com/homes/for_sale/"

driver = webdriver.Firefox()   ##verificar la version que firefox, tambien puede ser chrome 
driver.get(website)
time.sleep(1)

#datos=driver.find_element(By.CLASS_NAME,"List-c11n-8-100-4__sc-1smrmqp-0")
ls=input("ya dejaste de ser bot")
precio=[]
cuarto=[]
banio=[]
areaTerreno=[]
ubicacion=[]

next=driver.find_element(By.XPATH,'//a[@title="Next page"]')
for x in range(2,20):
    print("intentalo")
    time.sleep(7)
    
    extract=driver.find_elements(By.CLASS_NAME,"property-card")
    for y in extract:
        
        z=y.find_element(By.CLASS_NAME,"property-card-data")
        precio.append(z.find_element(By.XPATH,'//span[@data-test="property-card-price"]').text)
        ds=z.find_elements(By.TAG_NAME,"li")
        cuarto.append(ds[0].text)
        banio.append(ds[1].text)
        areaTerreno.append(ds[2].text)
        ubicacion.append(z.find_element(By.CLASS_NAME,"property-card-link").text)
    
    try:
        
        driver.find_element(By.XPATH,'//a[@title="Next page"]')
    except: print("que pena no se pudo")
driver.quit()

df=pd.DataFrame()
df['PRECIO']=precio
df['CUARTOS']=cuarto
df['BANIOS']=banio
df['AREA DEL TERRENO']=areaTerreno
df['UBICACION VIVIENDA']=ubicacion


df.to_csv("zillow1.csv",index=False)