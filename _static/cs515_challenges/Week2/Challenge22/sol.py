def print_emails(emails):
    for domain, names in emails.items():
        print('\n'.join([name + '@' + domain for name in names]))
        
# Or this:
def print_emails(emails):
    for (domain, users) in emails.items():
        for user in users:
            print(f'{user}@{domain}')