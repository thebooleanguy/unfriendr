from selenium import webdriver
from selenium.webdriver.common.by import By

from credentials import username, password

class unfriendr:
    def __init__(self):
        self.driver = webdriver.Firefox()


    def get_people(self):
        # container = self.driver.find_element(By.CLASS_NAME, '_a706')
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        names = [name.text for name in links if name.text != '']
        print(str(len(names)))
        return names

    def get_unfollowers(self):
        self.driver.get('file:///home/xany/Projects/python/unfriendr/data/followers.html')
        followers_list = self.get_people()
        self.driver.get('file:///home/xany/Projects/python/unfriendr/data/following.html')
        following_list = self.get_people()

        unfollowers_list = [user for user in following_list if user not in followers_list]
        unfollowers_list.sort()
        print(str(len(unfollowers_list)))
        print(unfollowers_list)

    def login(self, username, password):
        self.driver.get('https://instagram.com/')

        username_input = self.driver.find_element(By.XPATH, '//input[@name=\"username\"]')
        username_input.send_keys(username)

        password_input = self.driver.find_element(By.XPATH, '//input[@name=\"password\"]')
        password_input.send_keys(password)

        log_in = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[3]/button')
        log_in.click()


bot = unfriendr()
bot.get_unfollowers()
#bot.login(username, password)
