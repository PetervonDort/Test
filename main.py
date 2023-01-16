import time,re
from datetime import date
from selenium import webdriver
import sqlite3, locale
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Varibales
service = Service(executable_path="./chromedriver")
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=chrome_options)
aktuelleWoche = date.today().strftime("%W")
aktuellerTag = date.today().strftime("%a")
aktuelleStunde = time.strftime('%H')
locale.setlocale(locale.LC_ALL, '')
hour = int(aktuelleStunde)
Price_Peak = 0
Price_High = 0
Price_Low = 0
Down_Price = 0

class ClDatabase():
    def __init__(self):
        connection =sqlite3.connect("/home/peter/Dokumente/Datenbanken/Rechner.db")
        pointer = connection.cursor()
        sql_commands =""" 
        CREATE TABLE IF NOT EXISTS Kurse(
        Day TEXT(3),
        Hour INT(2),
        Minute TEXT(2),
        Price REAL(5),
        Price_Peak REAL(5),
        Price_High REAL(5),
        Price_Low REAL(5),
        Down_Price REAL (5)      
        );"""
        pointer.execute(sql_commands)


    def meKursupload(self,  Tag, Stunde, Minute,  Price,  Price_Peak, Price_High, Price_Low, Down_Price):
        verbindung = sqlite3.connect("/home/peter/Dokumente/Datenbanken/Rechner.db")
        zeiger = verbindung.cursor()
        zeiger.execute( """
        INSERT INTO Kurse VALUES(?,?,?,?,?,?,?,?)""",
                        ( Tag, Stunde, Minute,  Price,  Price_Peak, Price_High, Price_Low, Down_Price))
        verbindung.commit()
        verbindung.close()



class ClDatacollect():
    def __init__(self):
        driver.get("https://www.onvista.de/aktien/handelsplaetze/Deutsche-Telekom-Aktie-DE0005557508")
        time.sleep(3)
        driver.switch_to.frame(1)
        driver.find_element(By.CSS_SELECTOR, ".start-focus").click()
        driver.switch_to.parent_frame()

    def meGrab(self):
        contList = []
        helpList = []
        k =driver.find_elements(By.CLASS_NAME,"outer-spacing--xsmall-top")
        for r in k:
            contList.append(r)#(r.get_attribute("innerHTML"))
        #contList[3]=([float(s) for s in re.findall(r'-?\d+\.?\d*', contList[3])])
        #for r in contList[3]:
         #   helpList.append(r)
        return (contList[3])

    def meClose(self):
        driver.close()

DataB = ClDatabase()
DataCollector = ClDatacollect()
while hour >7 and hour <18:
    aktuelleMinute = time.strftime('%M')
    aktuelleStunde = time.strftime('%H')
    hour = int(aktuelleStunde)
    Price_Peak =Price_Peak+1
    #Price = DataCollector.meGrab()
    #DataB.meKursupload(aktuellerTag, aktuelleStunde, aktuelleMinute,Price, Price_Peak, Price_High, Price_Low, Down_Price )
    string = (DataCollector.meGrab())
    print(Price_Peak)

    print(string)
DataCollector.meClose()

