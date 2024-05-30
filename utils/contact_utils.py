from .email_utils import send_contact_message

# def contact_us_form(self, form, redirect):
#     name = form.cleaned_data['name']
#     email = form.cleaned_data['email']
#     phone_number = form.cleaned_data['phone_number']
#     message = form.cleaned_data['message']

#     print('form: ', form)
#     send_contact_message(
#         name, email, phone_number, message)
    

def contact_us_form(self, body, redirect):
    name = body["name"]
    email = body['email']
    phone_number = body['phoneNumber']
    message = body['message']

    print('formbody: ', body)
    send_contact_message(
        name, email, phone_number, message)
