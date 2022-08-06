from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time
from tokenize import String
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### PRODUCTS ###
## CHECK ##
# Controllo presenza device - id: 0
def checkDevice(driver, name):
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
def chackPrize(driver):
    textPrize = driver.find_element(By.CLASS_NAME, "price-container").text
    return textPrize.split()[0][1:]


# Presenza prodotti nel carrello - id: 2
def checkCartList(driver):
    cols = driver.find_elements(By.XPATH, "//td")
    cartList = []
    for i, col in enumerate(cols):
        if (i % 4 == 1):
            cartList.append(col.text)
    
    return cartList

# Calcolo totale - id: 3
def calctot(driver):
    driver.find_element(By.ID, "cartur").click()
    total = driver.find_element(By.ID, "totalp").text
    return total

# Controllo transizione - id: 4
def checktransition(driver, dictionary):
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

    driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
    
    #Controllo
    result = {}
    result['name'] = driver.find_element(By.ID, "name").text
    
    result['country'] = driver.find_element(By.ID, "country").text

    result['city'] = driver.find_element(By.ID, "city").text

    result['card'] = driver.find_element(By.ID, "card").text

    result['month'] = driver.find_element(By.ID, "month").text

    result['year'] = driver.find_element(By.ID, "year").text

    result = {}
    text = driver.find_element(By.CLASS_NAME, "lead").text.split("\n")
    result['name'] = text[3].split()[-1]

    result['amount'] = text[1].split()[1]

    result['card'] = text[2].split()[-1]

    result['date'] = text[4].split()[-1]
    
    #Invio dei dati
    return result

## ACTIONS ##
# Visione device - id: 5
def visione(driver, name):
    driver.find_element(By.LINK_TEXT, name).click() # seleziona cell
    
# Selezione categoria - id: 6
def selectCategory(driver, category):
    # itemc
    # Laptops
    # Monitors
    if(category == "Phones"):
        driver.find_element(By.ID, "itemc").click()
    else:
        driver.find_element(By.LINK_TEXT, category).click()

# Selezione device e basta - id: 7
def selectDevice(driver, name):
    #driver.find_element(By.CSS_SELECTOR, ".col-lg-4:nth-child(1) .card-img-top").click()
    driver.find_element(By.LINK_TEXT, name).click()

# Aggiungi al carrello - id: 8
def  AddtoCart(driver):
    #Schiaccia il bottone
    driver.find_element(By.LINK_TEXT, "Add to cart").click()
    
    #Schiaccia alert ok
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    #Vai alla home
    driver.find_element(By.ID, "nava").click()

# Visione carrello - id: 9
def openCart(driver):
    driver.find_element(By.ID, "cartur").click()
 
# Delete - id: 10
def delete(driver):
    driver.find_element(By.LINK_TEXT, "Delete").click()
    
# Place order - id: 11
def placeOrder(driver):
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

def countiteration(dictionarytoProcess):
    flag = False
    lunghezza = 1
    for value in dictionarytoProcess.values():
        for mini in value:
            for elem in mini.values():
            #print(elem)
             if(flag == True):
                 #print(elem)
                 xi = json.dumps(elem)
                 #print(xi)
                 x = xi.split(",")
                 print(x)
                 lunghezza = len(x)
                 flag = False     
            if(elem == "5"):
                #print(elem)
                flag = True      
    return lunghezza

def runner(driver, dictionry):
    n = countiteration(dictionry)
    outDict = {"array": []}
    for i in range(0, n):
        for actionDict in dictionry.get("array"):
            action = int(actionDict.get("id"))
            print(action)
            if action == 0:# Controllo presenza device - id: 0
                check = checkDevice(driver, actionDict.get("params")[0].get(str(i+1)))
                outDict.get("array").append({"id": str(action), "params": [{str(i+1): check}]})
                
            elif action == 1:# Controllo prezzo - id: 1    
                textPrice = chackPrize(driver)
                outDict.get("array").append({"id":  str(action), "params": [{str(i+1): textPrice}]})
                
            elif action == 2:# Presenza prodotti nel carrello - id: 2
                cartList = checkCartList(driver)
                outDict.get("array").append({"id":  str(action), "params": [{str(i+1): cartList}]})
            elif action == 3:# Calcolo totale - id: 3
                total = calctot(driver)
                outDict.get("array").append({"id":  str(action), "params": [{str(i+1): total}]})
            elif action == 4:# Controllo transizione - id: 4
                result = checktransition(driver, actionDict.get("params")[0].get(str(i+1)))
                print(result)
                outDict.get("array").append({"id":  str(action), "params": [{str(i+1): result}]})
            elif action == 5:# Visione device - id: 5 
                visione(driver, actionDict.get("params")[0].get(str(i+1)))
            elif action == 6:# Selezione categoria - id: 6
                selectCategory(driver, actionDict.get("params")[0].get(str(i+1)))
            elif action == 7:# Selezione device e basta - id: 7
                selectDevice(driver, actionDict.get("params")[0].get(str(i+1)))
            elif action == 8:# Aggiungi al carrello - id: 8
                AddtoCart(driver)
            elif action == 9:# Visione carrello - id: 9
                openCart(driver)
            elif action == 10:# Delete - id: 10
                delete(driver)
            elif action == 11:# Place order - id: 11
                placeOrder(driver)
    return outDict



def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])

    with webdriver.Chrome(executable_path=PATH, chrome_options=options) as driver:
        driver.implicitly_wait(10)
        driver.get("https://www.demoblaze.com/")
        
        selectCategory(driver, "Phones")
        cell = "Samsung galaxy s6"
        check = checkDevice(driver, cell)
        if check:
            selectDevice(driver, cell)
            print(chackPrize(driver))
        else:
            print("Device not correct")

        time.sleep(2)
        driver.quit()


class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        
        dictJson = json.loads(post_data)
        print(dictJson)
        
        # do calculations
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])

        outDict={}

        with webdriver.Chrome(executable_path=PATH, chrome_options=options) as driver:
            driver.implicitly_wait(10)
            driver.get("https://www.demoblaze.com/")
            outDict = runner(driver, dictJson)
            
        
        # send data
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(outDict), "utf-8"))
    

#Windows Path
PATH = "C:/Users/vedov/Downloads/chromedriver.exe"
#Mac Path
#PATH = ""

PORT = 8000
server = HTTPServer(('', PORT), HttpHandler)
print(f"Server running on port {PORT}")
server.serve_forever()


