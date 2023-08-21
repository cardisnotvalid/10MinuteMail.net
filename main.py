from temp_mail.temp_mail import TenMinuteMail


temp_mail = TenMinuteMail()
email = temp_mail.get_email_address()
content = temp_mail.get_email_content("welcome")

print(temp_mail.get_all_email_content())
print(temp_mail.get_last_email())