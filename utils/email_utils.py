from django.core.mail import send_mail

def send_contact_message(name, email, phone_number, message):
    send_mail(
        subject='Contact message from 3hf',
        message=f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\n\nMessage: {message}",
        from_email=email,
        recipient_list=['program@3hf.ngo'],
    )

    print("Sent message")