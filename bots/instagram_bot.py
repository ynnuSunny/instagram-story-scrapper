import re
import os
import time
import urllib.parse
import urllib

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import pandas as pd
import math
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from . import BaseBot, BaseServices



class Services:
    PC = BaseServices.INSTAGRAM_PC.value


    

class InstagramBot(BaseBot):
    ROOT_URL = "https://www.instagram.com/"

    
    XPATH_LOGIN_USERNAME = "//input[@name='username']"
    XPATH_LOGIN_PASSWORD = "//input[@name='password']"
    
    XPATH_NOTIFY_NOT_NOW = "//button[@class='_a9-- _ap36 _a9_1']"
    
    # i can do those xpath more optimize if i got enough time

    XPATH_START_STORY = '/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/div[1]/button[1]' 
    XPATH_NEXT_STORY = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[5]/section[1]/div[1]/button[@aria-label='Next']"
    XPATH_USER_NAME_STORY = "//div[@class='_ac0o']/div[2]//a" 
    XPATH_CONTENT_IMAGE_STORY = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/div[1]/div/div/img'                           
    XPATH_CONTENT_VIDEO_STORY = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/div[1]/div/div/div/div/div/div/video'
    XPATH_CONTENT_DATE_TIME = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/header/div[2]/div[1]/div/div[2]/div/div/time'

    def __init__(
        self, parameters, *args, **kwargs
    ):
        super(InstagramBot, self).__init__(
            parameters, *args, **kwargs
        )
        self.services = Services

    
        
    def login(self, username,password):
        time.sleep(3)

        username_field = self.driver.find_element(By.XPATH,self.XPATH_LOGIN_USERNAME)
        password_field = self.driver.find_element(By.XPATH,self.XPATH_LOGIN_PASSWORD)

        username_field.send_keys(username)
        time.sleep(self.TIME_INTERVAL_BASE)
        password_field.send_keys(password)
        time.sleep(self.TIME_INTERVAL_BASE)
        
        password_field.send_keys(Keys.RETURN)

        time.sleep(2.0)
        
 
    def fetch_instagram(self,URL):
        self._get(URL)
        self.login(self.user_name,self.password)
        time.sleep(self.TIME_INTERVAL_BASE)
        
        
    def get_instagram_story_user():
        # i can do this also if i get time.
        pass
    def give_like_and_comment():
        # i can do this also if i get enough time.
        pass

    def get_instagram_story_friends(self):
        
        for _ in range(5):
            notify_not_now = self.driver.find_elements(By.XPATH, self.XPATH_NOTIFY_NOT_NOW)
            if(len(notify_not_now)==0):
                print("There is no notify button")
                time.sleep(2)
            else:
                print("Notify button clicked")
                notify_not_now[0].click()
                break
                    


        time.sleep(10)

        # clink in the first story
        start_story_is_found = False
        for _ in range(20):
            start_story = self.driver.find_elements(By.XPATH, self.XPATH_START_STORY)
            if(len(start_story)==0):
                print("There is no strory!")
                time.sleep(2)
            else:
                print("Story button clicked")
                start_story[0].click()
                start_story_is_found = True
                time.sleep(1)
                break
                
                
        
        if start_story_is_found==False:
            return
            
        time.sleep(2)
        

        # clink button untill last story
        while(True):
            data = {}
            
            user_name = self.driver.find_elements(By.XPATH, self.XPATH_USER_NAME_STORY)
            if(len(user_name)!=0):
                data['user_name'] = user_name[0].text
                
            time.sleep(self.TIME_INTERVAL_BASE)

            try:       
                content_link = self.driver.find_element(By.XPATH,self.XPATH_CONTENT_VIDEO_STORY).get_attribute("src")
            except NoSuchElementException:
                time.sleep(self.TIME_INTERVAL_BASE)
                content_link = self.driver.find_element(By.XPATH,self.XPATH_CONTENT_IMAGE_STORY).get_attribute("src")
                is_video = False
            data['content'] = content_link

            date_time = self.driver.find_elements(By.XPATH, self.XPATH_CONTENT_DATE_TIME)
            if len(date_time)!=0: date_time = date_time[0].get_attribute('datetime')
            data['post-date'] = date_time

            self.friends_story_data.append(data)

            time.sleep(self.TIME_INTERVAL_BASE)
            next_story = self.driver.find_elements(By.XPATH, self.XPATH_NEXT_STORY)
            
            if(len(next_story)!=0):
                next_story[0].click()
                next_story = self.driver.find_elements(By.XPATH, self.XPATH_NEXT_STORY)
                if(len(next_story)==0): break
            else:
                break
        

    def get_pages_preprocess(self):
        entry_keyword = ""
        _entry_keyword = self.searched_keyword.replace("/", "-")
        self.entry_keyword = entry_keyword = urllib.parse.quote(entry_keyword)
        self.URL = self.ROOT_URL

    def get_pages(self, service):
        self.service = service
        # self.get_pages_preprocess()
        print(self.parameters)
        self.user_name = self.parameters.get("USER-NAME")
        self.password = self.parameters.get("PASSWORD")
        # print(self.URL)
        if(self.parameters.get('FRIENDS_STORY')):
            print("Fetching frines story")
            self.fetch_instagram(self.ROOT_URL)
            self.get_instagram_story_friends()
        # if(self.parameters.get('INDEVIDUAL_STORY')):
        #     print("Fethcing with user id")
        #     url = f'{self.ROOT_URL}stories/{self.parameters.get("USER_ID")}'
        #     self.fetch_instagram(url)
        #     self.get_instagram_story_user()

        
        return self.friends_story_data

