from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")
        elementById1 = driver.find_element_by_id("multiple-select-example")
        #elementById2 = driver.find_element_by_id("multiple-select-example2")
        elementByName = driver.find_element_by_name("show-hide")
        elementByClassName = driver.find_elements_by_class_name("block large-show-spacer")
        elementBySubID = driver.find_element_by_id("bmwradio")

        if elementById is not None:
            print("Test Passed: We found an element by Id")
        else:
            print("Test Failed : No element for Id has found")

        if elementById1 is not None:
            print("Test Passed: We found an element by Id1")
        else:
            print("Test Failed : No element for Id1 has found")

        # if elementById2 is not None:
        #     print("Test Passed: We found an element by Id2")
        # else:
        #     print("Test Failed : No element for Id2 has found")

        if elementByName is not None:
            print("Test Passed: We found an element by Name")
        else:
            print("Test Failed : No element for Name has found")

        if elementByClassName is not None:
            print("Test Passed: We found an element by Class Name")
        else:
            print("Test Failed : No element for Class Name has found")

# class FindBySubIdName(FindByIdName):

   # def test2(self):


        if elementBySubID is not None:
            print("Test Passed: We found an element 'bmwradio'")
        else:
            print("Test Failed : No bmwradio")


ff = FindByIdName()
ff.test()

# ff2 = FindBySubIdName
# ff2.test2()
