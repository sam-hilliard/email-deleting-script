import purge_emails
from time import sleep


#ensures that a valid gmail email is entered
def get_email():
    email = input('Enter your email: ')
    while True:
        if len(email) > 10 and email[-10:] == '@gmail.com' and not ' ' in email:
            break
        print('Gmail invalid.')
        email = input('Please enter a valid gmail: ')

    return email

# ensures given input is a number in the range 1-4
def in_range(num):
    
    while True:
        if num.isdigit() and int(num) > 0 and int(num ) < 5:
            break
        num = input('Please enter a valid option 1-4: ')

    return int(num)

#let's the user choose between 4 different browswers that work with the webdriver
def get_browser():
    print('What browser do you have installed: ')
    print('[1] Chrome')
    print('[2] Fire Fox')
    print('[3] Safari')
    print('[4] Opera')

    browser = input()
    browser = in_range(browser)

    return browser



def get_operation():
    print('\nChoose a delete operation: ')
    print('[1] Only keep starred mail')
    print('[2] Only keep imporant mail')
    print('[3] Keep both starred and imporant mail')
    print('[4] Delete all mail')

    operation = input()
    operation = in_range(operation)

    return operation

# main function handles user interaction and flow of the program
def main():
    print('Gmail inbox clearing tool \n by Sam Hilliard\n')

    email = get_email()
    password = input('Enter your password: ')
    operation = get_operation()
    browser = get_browser()

    print('Starting browser...')
    try:
        purger = purge_emails.EmailPurger(email, password, browser)
    except:
        print('Looks like you don\'t have a webdriver currently installed.')
        print('Follow the instructions linked below: ')
        print('For Chrome: https://chromedriver.chromium.org/downloads')
        print('For FireFox: https://github.com/mozilla/geckodriver/releases')
        print('For Safari: https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari')
        print('For Opera: https://github.com/operasoftware/operachromiumdriver/releases')
        print('If you\'re using Edge or Internet Explorer, do yourself a favor and get one of the browsers listed above.')
    print('Logging in with user, ' + email + ', and password, ' + password + '...')

    # give an error message if the login failed
    purger.login()

    print('Deleting specified emails...')
    sleep(10)

    # traverse through older emails to delete them
    can_next = True
    while(can_next):
        emails_remaining = True
        while(emails_remaining):
            emails_remaining = purger.delete_mail(operation)
        can_next = purger.next_page()
        sleep(5)

    print('Done!')
    purger.close()

main()

