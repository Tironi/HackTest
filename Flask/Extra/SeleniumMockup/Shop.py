from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import asyncio

PATH = "/Users/marcovinciguerra/Github/HackTest/Flask/ChromeDriver/chromedriver"


driver = webdriver.Chrome(PATH)
driver.get("https://www.demoblaze.com/")
driver.find_element(By.ID, "itemc").click()
driver.find_element(By.ID, "itemc").click()
driver.find_element(By.CSS_SELECTOR, ".col-lg-4:nth-child(1) .card-img-top").click()
driver.find_element(By.LINK_TEXT, "Add to cart").click()


