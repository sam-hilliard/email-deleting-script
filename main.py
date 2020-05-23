import purge_emails
from time import sleep

def main():
    print('Gmail inbox clearing tool \n by Sam Hilliard\n')
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    purger = purge_emails.EmailPurger(email, password)
    print('Logging in with user, ' + email + ', and password, ' + password + '...')
    purger.login()

    print('Deleting unimportant emails...')
    sleep(10)

    emails_remaining = True

    #traverse through older emails to delete them
    can_next = True
    while(can_next):
        while(emails_remaining):
            emails_remaining = purger.delete_mail()
        can_next = purger.next_page()
        sleep(5)
        #causes infinite loop
        emails_remaining = True

    #go back the other direction to delete older emails
    can_prev = True
    while(can_prev):
        while(emails_remaining):
            emails_remaining = purger.delete_mail()
        can_prev = purger.prev_page()
        sleep(5)
        emails_remaining = True

    print('Done!')
    purger.close()

main()