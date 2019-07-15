from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #create an instance of bot
        self.bot = webdriver.Firefox()


    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        #inspect page to look for unique identifier of an element to the find with bot.
        username = bot.find_element_by_xpath("//input[contains(@name,'username')]").send_keys(self.username)
        password = bot.find_element_by_xpath("//input[contains(@name,'password')]").send_keys(self.password)
        
        button = bot.find_element_by_class_name('submit')
        button.click()
        time.sleep(5)


    #switch to legacy twitter
    def switch_twitter(self):
        bot = self.bot
        time.sleep(5)
        button = bot.find_element_by_xpath("//div[@aria-label='More menu items']")
        button.click()
        time.sleep(5)
        switch = bot.find_element_by_xpath("//a[@href='/i/optout']")
        switch.click()


    def follow(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)

        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]

            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    follow_btn = bot.find_element_by_class_name('button-text.follow-text')
                    like_btn = bot.find_element_by_class_name('HeartAnimation')
                    follow_btn.click()
                    like_btn.click()
                    
                    """
                    if follow_btn.text != 'Following':
                        follow_btn.click()
                        like_btn.click()
                    else:
                        like_btn.click()
                    """

                    time.sleep(3)
                except Exception as ex:
                    time.sleep(10)
    

    def like(self):
        pass
    

    def retweet(self):
        pass
    
    
    def tweet(self):
        pass


bot = TwitterBot('email', 'password')
bot.login()
bot.follow('MetroFMBreakFast')