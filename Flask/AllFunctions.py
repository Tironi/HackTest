import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Windows Path
PATH = "C:/Users/vedov/Downloads/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

with webdriver.Chrome(executable_path=PATH, chrome_options=options) as driver:
    driver.implicitly_wait(10)
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click() # seleziona cell
    prezzo = driver.find_element(By.CLASS_NAME, "price-container").text
    driver.find_element(By.LINK_TEXT, "Add to cart").click()
    driver.find_element(By.ID, "cartur").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
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
    driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()

    time.sleep(2)
    driver.quit()

### PRODUCTS ###
## CHECK ##
# Controllo presenza device - id: 0
def checkDevice(name):
    found = False
    
    while True:
        try:
            driver.find_element(By.LINK_TEXT, name)
            found = True
            break
        except NoSuchElementException:
            if driver.find_element(By.ID, "next2").value_of_css_property("display") == "block":
                driver.find_element(By.ID, "next2").click()
            else:
                break
    return found

# Controllo prezzo - id: 1
def chackPrize():
    textPrize = driver.find_element(By.CLASS_NAME, "price-container").text
    return textPrize.split()[0][1:]


# Presenza prodotti nel carrello - id: 2
def checkCartList():
    cols = driver.find_elements(By.XPATH, "//td")
    cartList = []
    for i, col in enumerate(cols):
        if (i % 4 == 1):
            cartList.append(col.text)
    
    return cartList

# Calcolo totale - id: 3
def calctot():
    driver.find_element(By.ID, "cartur").click()
    total = driver.find_element(By.ID, "totalp").text
    return total

# Controllo transizione - id: 4
def checktransition(dictionary):
    #Inserimento dati
    driver.find_element(By.ID, "name").click()
    driver.find_element(By.ID, "name").send_keys(dictionary.get("name"))
    driver.find_element(By.ID, "country").click()
    driver.find_element(By.ID, "country").send_keys(dictionary.get("country"))
    driver.find_element(By.ID, "city").click()
    driver.find_element(By.ID, "city").send_keys(dictionary.get("city"))
    driver.find_element(By.ID, "card").click()
    driver.find_element(By.ID, "card").send_keys(dictionary.get("card"))
    driver.find_element(By.ID, "month").click()
    driver.find_element(By.ID, "month").send_keys(dictionary.get("month"))
    driver.find_element(By.ID, "year").click()
    driver.find_element(By.ID, "year").send_keys(dictionary.get("year"))

    #Controllo
    result = {}
    result['name'] = driver.find_element(By.ID, "name").text
    
    result['country'] = driver.find_element(By.ID, "country").text

    result['city'] = driver.find_element(By.ID, "city").text

    result['card'] = driver.find_element(By.ID, "card").text

    result['month'] = driver.find_element(By.ID, "month").text

    result['year'] = driver.find_element(By.ID, "year").text

    #Invio dei dati
    return result

## ACTIONS ##
# Visione device - id: 5
def visione(name):
    driver.find_element(By.LINK_TEXT, name).click() # seleziona cell
    
# Selezione categoria - id: 6
def selectCategory(category):
    # itemc
    # Laptops
    # Monitors
    if(category == "itemc"):
        driver.find_element(By.ID, "itemc").click()
    else:
        driver.find_element(By.LINK_TEXT, category).click()

# Selezione device e basta - id: 7
def selectDevice(name):
    #driver.find_element(By.CSS_SELECTOR, ".col-lg-4:nth-child(1) .card-img-top").click()
    driver.find_element(By.CSS_SELECTOR, "name").click()

# Aggiungi al carrello - id: 8
def  AddtoCart():
    #Schiaccia il bottone
    driver.find_element(By.LINK_TEXT, "Add to cart").click()
    
    #Schiaccia alert ok
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    #Vai alla home
    driver.find_element(By.ID, "nava").click()

# Visione carrello - id: 9
def openCart():
    driver.find_element(By.ID, "cartur").click()
 
# Delete - id: 10
def delete():
    driver.find_element(By.LINK_TEXT, "Delete").click()
    
# Place order - id: 11
def placeOrder():
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

def runner(listActionsId):
    for action in listActionsId:
        if action == 0:# Controllo presenza device - id: 0
            checkDevice(name)
        elif action == 1:# Controllo prezzo - id: 1    
            chackPrize()
        elif action == 2:# Presenza prodotti nel carrello - id: 2
            checkCartList()
        elif action == 3:# Calcolo totale - id: 3
            calctot()
        elif action == 4:# Controllo transizione - id: 4
            checktransition(dictionary)
        elif action == 5:# Visione device - id: 5 
            visione(name)
        elif action == 6:# Selezione categoria - id: 6
            selectCategory(category)
        elif action == 7:# Selezione device e basta - id: 7
            selectDevice(name)
        elif action == 8:# Aggiungi al carrello - id: 8
            AddtoCart()
        elif action == 9:# Visione carrello - id: 9
            openCart()
        elif action == 10:# Delete - id: 10
            delete()
        elif action == 11:# Place order - id: 11
            placeOrder()
        

#form insert
def form():
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
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

# pay
def Pay():
    driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
    
def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])

    with webdriver.Chrome(executable_path=PATH, chrome_options=options) as driver:
        driver.implicitly_wait(10)
        driver.get("https://www.demoblaze.com/cart.html")
        
        runner()