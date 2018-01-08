from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        xpath1 = "//div[@id='navbar']//a[@href='/sign_in']"
        emailadd1 = 'test'
        emailadd2 = 'ganern'
        pword1 = 'ewan'

        loginLink = driver.find_element(By.XPATH, xpath1)
        time.sleep(3)
        print("Login link element has been found")
        loginLink.click()
        print("Clicking Login link")


        emailField = driver.find_element(By.ID, "user_email")
        print("Typing email address in 5 sec")
        time.sleep(5)
        emailField.send_keys(emailadd1)


        passwordField = driver.find_element(By.ID, "user_password")
        time.sleep(3)
        passwordField.send_keys(pword1)

        time.sleep(5)

        emailField.clear()

        time.sleep(5)

        emailField.send_keys(emailadd2)



ff = ClickAndSendKeys()
ff.test()