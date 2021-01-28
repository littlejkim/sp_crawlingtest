from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.netflix.com")

browser.find_element_by_xpath(
    '//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a').click()

email = browser.find_element_by_id("id_userLoginId")
password = browser.find_element_by_id("id_password")

email.send_keys("rlqkrwls@naver.com")
password.send_keys("uhd6800!")

password.send_keys(Keys.RETURN)

browser.implicitly_wait(15)
browser.find_elements_by_class_name('profile-icon')[0].click()
browser.implicitly_wait(15)
browser.get("https://www.netflix.com/YourAccountPayment")

cardNumber = browser.find_element_by_id("id_creditCardNumber")
expirationDate = browser.find_element_by_id("id_creditExpirationMonth")
cardHolderName = browser.find_element_by_id("id_name")

cardNumber.send_keys('1234')
expirationDate.send_keys('123')
cardHolderName.send_keys('John Kim')
time.sleep(3)

browser.quit()
