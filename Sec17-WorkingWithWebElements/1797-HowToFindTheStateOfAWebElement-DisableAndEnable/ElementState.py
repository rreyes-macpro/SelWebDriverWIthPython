from selenium import webdriver

class ElementState():

    def isEnabled(self):
        baseUrl = "http://www.google.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        inputtxt = "letsgo"

        e1 = driver.find_element_by_id("lst-ib")
        e1State = e1.is_enabled() # True for enabled and False for disabled
        print("E1 is Enabled? -> " + str(e1State))
        if e1State == True:
            print("E1 Id is ENABLED, we CAN automate type input on this textbox")
            e1.send_keys(inputtxt)
        else:
            print("E1 Id is DISABLED, we CANNOT automate type input on this textbox")

        e2 = driver.find_element_by_id("gs_taif0")
        e2State = e2.is_enabled()  # True for enabled and False for disabled
        print("E2 is Enabled? -> " + str(e2State))
        if e2State == True:
            print("E2 Id is ENABLED, we CAN automate type input on this textbox")
            e2.send_keys(inputtxt)
        else:
            print("E2 Id is DISABLED, we CANNOT  automate type input on this textbox")

        e3 = driver.find_element_by_id("gs_htif0")
        e3State = e3.is_enabled()  # True for enabled and False for disabled
        print("E3 is Enabled? -> " + str(e3State))
        if e3State == True:
            print("E3 Id is ENABLED, we CAN automate type input on this textbox")
            e3.send_keys(inputtxt)
        else:
            print("E3 Id is DISABLED, we CANNOT  automate type input on this textbox")



e = ElementState()
e.isEnabled()