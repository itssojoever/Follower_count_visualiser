import lxml
import json
import os
from apscheduler.schedulers.background import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def scheduler():
    if os.path.isfile("config.json"):
        print("Config found")
        with open ("config.json") as f:
            try:
                data = json.load(f)
                timeH = data.get("hour")
                timeM = data.get("minutes")
                scheduler = BlockingScheduler()
                job_1 = scheduler.add_job(scrapeData, hour = timeH , minute= timeM)
                scheduler.start()
            except json.JSONDecodeError:
                print ("Config file exists but is not complete, please relaunch config")

    

def scrapeData():

    firefoxOptions = Options()
    firefoxOptions.add_argument("--headless")
    url = input("Please input desired site : ")
    driver = webdriver.Firefox(options=firefoxOptions)
    driver.get(url)

    resultOfRequest = BeautifulSoup(driver.page_source, "lxml")

    metaTag = resultOfRequest.find("meta", attrs={"name" : "description"})
    content = metaTag["content"]

    followerInfo = content.split("Followers,")[0].strip()
    followerCount = followerInfo.split()[0].replace(",", "")

    print(followerCount)