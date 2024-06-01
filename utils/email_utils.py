from django.core.mail import EmailMessage
from django.conf import settings


def send_contact_message(name, email, phone_number, message):
    subject = 'Contact message from 3hf'
    message_body = f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\n\nMessage: {message}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    reply_to = [email,]

    email_message = EmailMessage(
        subject=subject,
        body=message_body,
        from_email=from_email,
        to=recipient_list,
        reply_to=reply_to,
    )
    email_message.send()

    print("Sent message")
