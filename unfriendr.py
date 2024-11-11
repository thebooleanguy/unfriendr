from selenium import webdriver
from selenium.webdriver.common.by import By

from credentials import username, password

class unfriendr:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get('https://instagram.com/')

        username_input = self.driver.find_element(By.XPATH, '//input[@name=\"username\"]')
        username_input.send_keys(username)

        password_input = self.driver.find_element(By.XPATH, '//input[@name=\"password\"]')
        password_input.send_keys(password)

        log_in = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[3]/button')
        log_in.click()

bot = unfriendr(username, password)
