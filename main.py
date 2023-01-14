import time
from selenium import webdriver
import sqlite3 ,locale
#frome datetime import date
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Varibales
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

class ClDatabase():
    def __init__(self):
        connecting = sqlite3.connect("home/peter/Dokumente/datenbanken/boerseRechner.db")
        pointer = connecting.cursor()
        sql_command="""
        CREATE TABLE IF NOT EXIST share_price(
        Week TEXT(3),
        Day TEXT(3),
        Max_Price REAL(5)
        );"""
        pointer.execute(sql_command)

class ClDatacollect():
    def __init__(self):
        driver.get("https://www.onvista.de/aktien/handelsplaetze/Deutsche-Telekom-Aktie-DE0005557508")
        time.sleep(3)
        driver.switch_to.frame(1)
        driver.find_element(By.CSS_SELECTOR, ".start-focus").click()
        driver.switch_to.parent_frame()
    def meGrab(self):
        contList = []
        k =driver.find_elements(By.CLASS_NAME,"outer-spacing--xsmall-top")
        for r in k:
            contList.append((r.get_attribute("innerHTML")))
        return (contList[3])



#DataB = ClDatabase()

DataCollector = ClDatacollect()
print(DataCollector.meGrab())
