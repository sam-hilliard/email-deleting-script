from selenium import webdriver
from time import sleep
import bs4 as bs

class EmailPurger:

    def __init__(self, email, password):
        self.driver = webdriver.Firefox()
        self.email = email
        self.password = password

    def login(self):
        #navigating to login page
        self.driver.get('https://www.google.com/gmail')
        sleep(5)

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
    def delete_mail(self, operation):
        #get the html source for soup to parse through
        html = self.driver.page_source
        soup = bs.BeautifulSoup(html, 'html.parser')
        emails = soup.find_all('tr', attrs={'class':'zA'})
        delete = False
        
        for email in emails:
            contents = str(email.contents)

            #option 1: keep only starred emails
            if operation == 1:
                if 'Not starred' in contents:
                    delete = True

            #option 2: keep only important emails
            if operation == 2:
                if 'Not important' in contents:
                    delete = True
            
            #option 3: keep both starred and important emails
            if operation == 3:
                if 'Not important' in contents and 'Not starred' in contents:
                    delete = True

            #option 4: delete all mail
            if (operation == 4):
                delete = True

            if delete:
                checkbox_id = email.find('div', attrs={'role':'checkbox'}).get('id')
                checkbox = self.driver.find_element_by_id(checkbox_id)
                try:
                    checkbox.click()
                except:
                    sleep(3)
    
        #click delete button
        try:
            delete_button = self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div[3]/div')
            delete_button.click()
            sleep(5)
        except:
            return False

        return True

    #navigates to the next page once all emails are deleted
    def next_page(self):
        next = self.driver.find_element_by_id(':la')

        html = self.driver.page_source
        soup = bs.BeautifulSoup(html, 'html.parser')
        next_html = soup.find('div', attrs={'id':':la'})

        if 'aria-disabled="true"' in str(next_html):
            return False

        next.click()
        return True
    
    #closes the browser window  
    def close(self):
        self.driver.close()

    #fills a text field with a given input
    def fill_field(self, input, field_path, btn_path):
        field = self.driver.find_element_by_xpath(field_path)
        field.send_keys(input)
        sleep(2)
        btn = self.driver.find_element_by_xpath(btn_path)
        btn.click()
