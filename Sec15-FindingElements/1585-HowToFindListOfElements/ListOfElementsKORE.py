from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseUrl = "https://jobs.jobvite.com/koretelematics"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        # elementListByClassName = driver.find_elements_by_class_name("inputs")
        # length1 = len(elementListByClassName)
        #
        # if elementListByClassName is not None:
        #     print("ClassName -> Size of the list is: " + str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("TagName -> Size of the list is: " + str(length2))

        elementListByTagName3 = driver.find_elements(By.TAG_NAME, "tr")
        length3 = len(elementListByTagName3)
        listit = elementListByTagName3

        if elementListByTagName3 is not None:
            print("TagName -> Size of the list is: " + str(length3))

        a = "table>tbody>tr>td[class$='location'"
        elementListByTagName4 = driver.find_elements(By.CLASS_NAME, a)
        length4 = len(elementListByTagName4)

        if elementListByTagName4 is not None:
            print("TagName -> Size of the list is: " + str(length4))
            for x in elementListByTagName4:
                print(x)


        #driver.close()

ff = ListOfElements()
ff.test()