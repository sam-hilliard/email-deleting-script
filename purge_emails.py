from selenium import webdriver
from time import sleep
import bs4 as bs

class EmailPurger:

    def __init__(self, e, p):
        self.driver = webdriver.Firefox()
        self.email = e
        self.password = p

    def login(self):
        #navigating to login page
        self.driver.get('https://www.google.com/gmail')
        sleep(5)
        #sign_in = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a')
        #sign_in.click()


        #filling out the email field
        email_xpath = '//*[@id="identifierId"]'
        next_btn_path = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span'
        self.fill_field(self.email, email_xpath, next_btn_path)
        sleep(5)

        #filling out the password field
        pass_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
        next_btn_path = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span'
        self.fill_field(self.password, pass_xpath, next_btn_path)

    #deletes mail until there is no more mail 
    def delete_mail(self):
        #let the page load
        sleep(10)
        #get the html source for soup to parse through
        html = self.driver.page_source
        soup = bs.BeautifulSoup(html, 'html.parser')
        emails = soup.find_all('tr', attrs={'class':'zA'})

        #loop through each email stored in a table row
        for email in emails:
            contents = str(email.contents)

            if "Not starred" in contents and "Not important" in contents:
                checkbox_id = email.find('div', attrs={'role':'checkbox'}).get('id')
                checkbox = self.driver.find_element_by_id(checkbox_id)
                checkbox.click()
        
        #click delete button
        delete_button = self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div[3]/div')
        delete_button.click()
        sleep(5)

    #fills a text field with a given input
    def fill_field(self, input, field_path, btn_path):
        field = self.driver.find_element_by_xpath(field_path)
        field.send_keys(input)
        sleep(2)
        btn = self.driver.find_element_by_xpath(btn_path)
        btn.click()
