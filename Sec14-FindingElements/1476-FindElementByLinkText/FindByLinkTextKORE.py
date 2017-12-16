from selenium import webdriver
from selenium.webdriver.common.by import By


class FindByLinkText():
    def test(self):
        baseUrl = "https://jobs.jobvite.com/koretelematics"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        # elementByLinkText1 = driver.find_element_by_link_text("Login")
        #
        # if elementByLinkText1 is not None:
        #     print("We found an element by Link Text1")
        #     print("The element by LinkText1 we found is \"" + str(elementByLinkText1.text) + '"')
        # else:
        #     print("We did not find an element by Link Text1")
        #     #print("The element by LinkText1 we found is \"" + str(elementByLinkText1.text) + '"')

        elementByLinkText2 = driver.find_element(By.LINK_TEXT, "QA Test Analyst")

        if elementByLinkText2 is not None:
            print("We found an element by Link Text2")
            print("The element by LinkText2 we found is \"" + str(elementByLinkText2.text) + '"')
        else:
            print("We did not find an element by Link Text2")
            # print("The element by LinkText2 we found is \"" + str(elementByLinkText2.text) + '"')

        elementByPartialLinkText1 = driver.find_element_by_partial_link_text("Soft")

        if elementByPartialLinkText1 is not None:
            print("We found an element by Partial Link Text1")
            print("The element by Partial Link Text we found is \"" + str(elementByPartialLinkText1) + '"')
        else:
            print("We did not find an element by Partial Link Text1")


ff = FindByLinkText()
ff.test()
