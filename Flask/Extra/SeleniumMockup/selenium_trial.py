from selenium import webdriver
import time 

#MACOS path
PATH = "/Users/marcovinciguerra/Github/HackTest/Flask/ChromeDriver/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/")
print("ciao")
driver.find_element_by_id("L2AGLb").click()
search = driver.find_element_by_id("input")
search.send_keys("input")
search.send_keys(Keys.ENTER)

time.sleep(2)
driver.quit()

