import requests
import lxml
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

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


#if resultOfRequest.status_code == 200:
#    result = BeautifulSoup(resultOfRequest.content, "lxml")
#    followerCount = result.find("span", class_="_ac2a")
#    print(followerCount)
#else:
#    print ("Error with status code: ", resultOfRequest.status_code)