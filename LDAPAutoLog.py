#!/usr/bin/python3.6
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()


def site_login(logData):
    driver.get("https://10.1.0.10:8090/httpclient.html")
    for uname, pwd in logData:
        try:
            if driver.find_element_by_id("msgDiv").text == "You have successfully logged in":
                break
            driver.find_element_by_name("username").clear()
            driver.find_element_by_name("password").clear()

            driver.find_element_by_name("username").send_keys(uname)
            driver.find_element_by_name("password").send_keys(pwd)

            driver.find_element_by_name("btnSubmit").click()
            sleep(0.4)
        except NoSuchElementException:
            driver.find_element_by_name("username").send_keys(uname)
            driver.find_element_by_name("password").send_keys(pwd)

            driver.find_element_by_name("btnSubmit").click()
            sleep(0.4)


if __name__ == "__main__":
    logData = [('uname1', 'pass1')]

    site_login(logData)
    driver.close()
