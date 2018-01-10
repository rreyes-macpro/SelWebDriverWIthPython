from selenium import webdriver
import time


class RadButtAndChkbx():

    def test1(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        t1 = 3 # seconds to wait before loading next command

        '''
        Testing Radio Buttons
        '''


        print('*' * 20 + "Testing Radio Buttons")
        bmwRadBtn = driver.find_element_by_id("bmwradio")
        print("Will select and click BMS radio button after "+ str(t1)+" seconds")
        time.sleep(t1)
        bmwRadBtn.click()

        benzRadBtn = driver.find_element_by_id("benzradio")
        print('Will select and click Benz radio button after ' + str(t1) + " seconds")
        time.sleep(t1)
        benzRadBtn.click()

        hondaRadBtn = driver.find_element_by_id("hondaradio")
        print("Will select and click Honda radio button after " + str(t1) + " seconds")
        time.sleep(t1)
        hondaRadBtn.click()

        '''
            Testing Check Boxes
        '''
        print('%' * 20 + "Testing Checkboxes")

        bmwChkbx = driver.find_element_by_id("bmwcheck")
        print("Will select and click BMW Checkbox after " + str(t1) + " seconds")
        time.sleep(t1)
        bmwChkbx.click()

        benzChkbx = driver.find_element_by_id("benzcheck")
        print("Will select and click Benz Checkbox after " + str(t1) + " seconds")
        time.sleep(t1)
        benzChkbx.click()

        hondaChkbx = driver.find_element_by_id("hondacheck")
        print("Will select and click Honda Checkbox after " + str(t1) + " seconds")
        time.sleep(t1)
        hondaChkbx.click()


        time.sleep(t1)

        print("BMW Radio button is selected? " + str(bmwRadBtn.is_selected()))  # True if selected, False is not selected
        print("Benz Radio button is selected? " + str(benzRadBtn.is_selected()))
        print("BMW Checkbox is selected? " + str(bmwChkbx.is_selected()))
        print("Benz Checkbox is selected? " + str(benzChkbx.is_selected()))


ff = RadButtAndChkbx()
ff.test1()

