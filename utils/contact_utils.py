from .email_utils import send_contact_message


def successResponse(body):
    return {
        'message':
        f"Hi, {body['name'].title()}, thank you for reaching out to us. We'll be in touch shortly.",
        "success": True
    }


def send_message(self, body, redirect):
    name = body["name"]
    email = body['email']
    phone_number = body['phoneNumber']
    message = body['message']

    print('formbody: ', body)
    send_contact_message(
        name, email, phone_number, message)
