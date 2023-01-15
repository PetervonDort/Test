import time
import re
from selenium import webdriver
import sqlite3 ,locale
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Varibales
service = Service(executable_path="./chromedriver")
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=chrome_options)

class ClDatabase():
    def __init__(self):
        connecting = sqlite3.connect("home/peter/Dokumente/Datenbanken/boerseRechner.db")
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
        helpList = []
        k =driver.find_elements(By.CLASS_NAME,"outer-spacing--xsmall-top")
        for r in k:
            contList.append((r.get_attribute("innerHTML")))
        contList[3]=([float(s) for s in re.findall(r'-?\d+\.?\d*', contList[3])])
        for r in contList[3]:
            helpList.append(r)
        return (helpList[0])



#DataB = ClDatabase()

DataCollector = ClDatacollect()
string = (DataCollector.meGrab())
print(string)
