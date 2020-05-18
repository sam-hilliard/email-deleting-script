import purge_emails

print('initializing...')
purger = purge_emails.EmailPurger('samhilliard51@gmail.com', 'schoolBoiSquid21')

print('logging in...')
purger.login()

print('testing delete_mail()...')
purger.delete_mail()

purger.driver.close()