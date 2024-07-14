from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from post_generation import GeneratePost
from dotenv import load_dotenv
from post_customization import Themes
import time
import os

load_dotenv()

email = os.environ.get('email_X')
password = os.environ.get('password')
username = os.environ.get('username')
URL = "https://x.com/"


class XBot:
    def __init__(self, theme):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(URL)

        theme_generator = Themes()
        temporal_theme = theme_generator.get_theme()
        business_theme = theme

        generate_post = GeneratePost(business=business_theme, temporal_theme=temporal_theme)

        time.sleep(2)

        self.post_ready = generate_post.create_post()
        self.connection_process()
        self.posting_process()

    def connection_process(self):
        connection = self.driver.find_element(By.LINK_TEXT, 'Se connecter')
        connection.click()
        time.sleep(2)
        email_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                         '/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/'
                                                         'div[2]/div/input')
        email_input.send_keys(email)
        connection_next = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                   '/div/div/div[2]/div[2]/div/div/div/button[2]')
        connection_next.click()
        time.sleep(2)
        try:
            insert_password = self.driver.find_element(By.XPATH,
                                                       '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                       '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label'
                                                       '/div/div[2]/div[1]/input')
            insert_password.send_keys(password)
            insert_password.send_keys(Keys.ENTER)

        except NoSuchElementException:
            insert_profile_name = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div'
                                                                     '/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]'
                                                                     '/div/div[2]/label/div/div[2]/div/input')
            insert_profile_name.send_keys(username)
            insert_profile_name.send_keys(Keys.ENTER)

            time.sleep(3)
            insert_password = self.driver.find_element(By.XPATH,
                                                       '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                       '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label'
                                                       '/div/div[2]/div[1]/input')
            insert_password.send_keys(password)
            insert_password.send_keys(Keys.ENTER)

    def posting_process(self):
        time.sleep(5)
        posting_window = self.driver.find_element(By.XPATH,
                                                  '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div'
                                                  '/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div'
                                                  '/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]'
                                                  '/div/div/div/div')
        posting_window.send_keys(self.post_ready)
        time.sleep(2)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div'
                                                         '/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]'
                                                         '/div[2]/div/div/div/button')
        time.sleep(2)
        post_button.click()
