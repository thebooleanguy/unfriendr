from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import json

from config import username, password, unfollow_amount, exceptions

class unfriendr:
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.options)
        self.unfollowers = []
        self.fname = "unfollowers.json"
        self.load_from_file()
        # self.unfollowers = set(self.unfollowers) - set(exceptions)
        self.unfollowers = [user for user in self.unfollowers if user not in exceptions]

    def load_from_file(self):
        try:
            file = open(self.fname,"r")
            print ("Unfollowers list found. Proceeding...")
            with file:
                 self.unfollowers = json.loads(file.read())
        except FileNotFoundError:
            print ("Creating unfollowers list...") 
            self.get_unfollowers()
        except OSError:
            print("Could not create file.")
            exit()

    def save_to_file(self):
        try:
            file = open(self.fname, "w")
            # print ("Saving unfollowers list...")
            with file:
                json.dump(self.unfollowers, file)
        except OSError:
            print ("Could not write to file.")
            exit()

    def get_followers(self):
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        names = [name.text for name in links if name.text != '']
        print("Followers: ", str(len(names)))
        return names

    def get_unfollowers(self):
        self.driver.get('file:///home/xany/Projects/python/unfriendr/data/followers.html')
        followers_list = self.get_followers()
        self.driver.get('file:///home/xany/Projects/python/unfriendr/data/following.html')
        following_list = self.get_followers()

        self.unfollowers = [user for user in following_list if user not in followers_list]
        self.unfollowers.sort()
        print("Unfollowers: ", str(len(self.unfollowers)))
        self.save_to_file()

    def login(self, username, password):
        self.driver.get('https://instagram.com/')

        sleep(2)
        # username_input = self.driver.find_element(By.XPATH, '//input[@name=\"username\"]')
        username_input = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[1]/div/label/input')
        username_input.send_keys(username)

        # password_input = self.driver.find_element(By.XPATH, '//input[@name=\"password\"]')
        password_input = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[2]/div/label/input')
        password_input.send_keys(password)

        log_in_btn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[3]/button')
        log_in_btn.click()
        sleep(8)

    def start_unfollowing(self, unflw_amnt):
        for i in self.unfollowers[:unflw_amnt]:
            if (self.unfollow_account(i) == 0):
                self.unfollowers.remove(i)
                self.save_to_file()
                sleep(30)
        # sleep(3600)
        # self.start_unfollowing()
        print("Unfollowed ~" + str(unflw_amnt) + " accounts.")
        self.driver.close()

    def unfollow_account(self, username):
        account_url = "https://instagram.com/" + username
        # print(account_url)
        self.driver.get(account_url)
        sleep(4)
        try:
            sleep(3)

            more_options_btn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button')
            sleep(3)
            more_options_btn.click()

        except NoSuchElementException:
            print(username + " is not a valid username")
            return 0
        sleep(4)
        try:
            sleep(3)
            unfollow_btn = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div[1]/div/div')

            sleep(3)
            unfollow_btn.click()
        except NoSuchElementException:
            print(username + " already unfollowed")
            return 0
        sleep(2)
        print(username + " Unfollowed ")
        return 0


bot = unfriendr()
bot.login(username, password)
bot.start_unfollowing(unfollow_amount)
# print(len(bot.unfollowers))
# print(len(bot.unfollowers_new))
