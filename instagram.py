from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Firefox()
        self.email = email
        self.password = password

    def signIn(self):
        browser = self.browser
        browser.get('https://www.instagram.com/accounts/login/')

        emailInput = browser.find_element_by_name('username').send_keys(self.email)  
        passwordInput = browser.find_element_by_name('password').send_keys(self.password)
        
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)


bot = InstagramBot('', '')
bot.signIn()