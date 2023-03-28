from email.message import EmailMessage
import ssl
import smtplib

from config import DiscountsConfig


class DiscountEmailSender:

    def __init__(self, config: DiscountsConfig) -> None:
        self.__target_email = config.get_config('inputs.email.target_email')
        self.__subject = config.get_config('inputs.email.subject')
        self.__source_email = config.get_config('inputs.email.source_email')
        self.__source_email_app_password = config.get_config('inputs.email.source_email_app_password')

        self.__ssl_context = ssl.create_default_context()

        print(f"""
        Going to use this config to send email:
         - Source mail: {self.__source_email}
         - Target mail: {self.__target_email}
        """)

    def send_discounts_mail(self, categories):
        mail = EmailMessage()
        mail['From'] = self.__source_email
        mail['To'] = self.__target_email
        mail['Subject'] = self.__subject
        mail.set_content(compose_mail_text(categories))
    
        with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=self.__ssl_context) as smtp:
            smtp.login(self.__source_email, self.__source_email_app_password)
            smtp.sendmail(self.__source_email, self.__target_email, mail.as_string())

        print(f'Email sent to {self.__target_email} about discounts!')


def compose_mail_text(categories) -> str:
    body = 'The following discounts were found:\n\n'
    for category in categories:
        body += str(category)
    body += '\n\nThis mail was sent from Python :)'
    return body
