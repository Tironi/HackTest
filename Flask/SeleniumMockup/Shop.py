from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import asyncio

PATH = "/Users/marcovinciguerra/Github/HackTest/Flask/ChromeDriver/chromedriver"

async def main():
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click() # seleziona cell
    #time.sleep(10) 
    await asyncio.sleep(5)

    driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click() # seleziona cell
    """time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Add to cart").click()
    time.sleep(1)
    driver.find_element(By.ID, "cartur").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    time.sleep(1)
    driver.find_element(By.ID, "name").click()
    driver.find_element(By.ID, "name").send_keys("matteo")
    driver.find_element(By.ID, "country").click()
    driver.find_element(By.ID, "country").send_keys("italia")
    driver.find_element(By.ID, "city").click()
    driver.find_element(By.ID, "city").send_keys("bergamo")
    driver.find_element(By.ID, "card").click()
    driver.find_element(By.ID, "card").send_keys("12345")
    driver.find_element(By.ID, "month").click()
    driver.find_element(By.ID, "month").send_keys("22")
    driver.find_element(By.ID, "year").click()
    driver.find_element(By.ID, "year").send_keys("23")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
    time.sleep(1)"""

main()
