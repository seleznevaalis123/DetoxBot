from django.core.mail import EmailMessage

EmailMessage('Subject', 'Body', 'selezneva.test@gmail.com', ['selezneva.test@gmail.com']).send()
