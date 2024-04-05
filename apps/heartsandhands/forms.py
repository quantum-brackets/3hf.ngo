
from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=13, required=False)
    message = forms.CharField(widget=forms.Textarea)

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data['phone_number']
    #     # Add any custom phone number validation here if needed
    #     return phone_number