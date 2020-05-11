from selenium import webdriver
from time import sleep

class EmailPurger:

    def __init__(self, e, p):
        self.driver = webdriver.Firefox()
        self.email = e
        self.password = p

    def login(self):
        self.driver.get('https://mail.google.com/')
        sleep(5)

        #filling out the email field
        email_xpath = '//*[@id="identifierId"]'
        next_btn_path = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span'
        self.fill_field(self.email, email_xpath, next_btn_path)
        sleep(5)

        #filling out the password field
        pass_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
        next_btn_path = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span'
        self.fill_field(self.password, pass_xpath, next_btn_path)
        sleep(5)

    def fill_field(self, input, field_path, btn_path):
        field = self.driver.find_element_by_xpath(field_path)
        field.send_keys(input)
        btn = self.driver.find_element_by_xpath(btn_path)
        btn.click()
