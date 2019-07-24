from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Facebook:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://facebook.com/')
        time.sleep(3)
        username = bot.find_element_by_name('email').send_keys(self.username)
        password = bot.find_element_by_name('pass').send_keys(self.password)

        button = bot.find_element_by_css_selector("input[type=submit]")
        button.click()
        time.sleep(3)

bot = Facebook('', '')
bot.login()