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
    def delete_mail(self):
        mail_deleted = False
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
                #waits for pop up to disappear if it is in the way of the checkbox
                try:
                    checkbox.click()
                except:
                    return False

                mail_deleted = True
        
        #click delete button
        try:
            delete_button = self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div[3]/div')
            delete_button.click()
            sleep(5)
        except:
            return False

        return mail_deleted

    #navigates to the next page once all emails are deleted
    def next_page(self):
        next = self.driver.find_element_by_id(':la')

        html = self.driver.page_source
        soup = bs.BeautifulSoup(html, 'html.parser')
        next_html = soup.find('div', attrs={'id':':la'})

        if "disabled" in str(next_html.contents):
            return False
        else:
            next.click()
            return True
    
    #goes to the previous page in inbox
    def prev_page(self):
        prev = self.driver.find_element_by_id(':l9')

        html = self.driver.page_source
        soup = bs.BeautifulSoup(html, 'html.parser')
        prev_html = soup.find('div', attrs={'id':':l9'})

        if "disabled" in str(prev_html.contents):
            return False
        else:
            prev.click()
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
