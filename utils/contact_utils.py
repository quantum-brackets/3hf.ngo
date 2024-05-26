from .email_utils import send_contact_message

def contact_us_form(self, form, redirect):
    if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            send_contact_message(
                name, email, phone_number, message)

            return redirect('home')
    else:
        # If the form is not valid, re-render the page with the form and errors
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)