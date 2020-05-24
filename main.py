import purge_emails
from time import sleep

def main():
    print('Gmail inbox clearing tool \n by Sam Hilliard\n')
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    print('\nChoose a delete operation: ')
    print('[1] Only keep starred mail')
    print('[2] Only keep imporant mail')
    print('[3] Keep both starred and imporant mail')
    print('[4] Delete all mail')
    operation = input()
    print('operation ' + operation + ' selected')
    operation = int(operation)

    purger = purge_emails.EmailPurger(email, password)
    print('Logging in with user, ' + email + ', and password, ' + password + '...')
    purger.login()

    print('Deleting specified emails...')
    sleep(10)

    emails_remaining = True

    #traverse through older emails to delete them
    can_next = True
    while(can_next):
        while(emails_remaining):
            emails_remaining = purger.delete_mail(operation)
        can_next = purger.next_page()
        sleep(5)
        emails_remaining = True

    print('Done!')
    purger.close()

main()