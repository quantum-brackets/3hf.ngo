from django.db import models
from django.core.exceptions import ValidationError


class EventRegistrationManager(models.Manager):
    def create_registrant(self, **kwargs):
        event_id = kwargs.pop('event_id')
        registrant_name = kwargs.pop('registrant_name')
        registrant_email = kwargs.pop('registrant_email')
        registrant_phone_number = kwargs.pop('registrant_phone_number')
        additional_message = kwargs.pop('additional_message')

        if not registrant_email:
            raise ValidationError('Email is required')
        if not registrant_name:
            raise ValidationError('Full name is required')
        if not registrant_phone_number:
            raise ValidationError('Phone number is required')


        if self.filter(
            event_id=event_id,
            registrant_email=registrant_email.lower(),
            registrant_phone_number=registrant_phone_number).exists():
            raise ValidationError(
                'Sorry, You are already registered for this event.')
        
        return self.create(
            event_id=event_id,
            registrant_name=registrant_name,
            registrant_email=registrant_email,
            registrant_phone_number=registrant_phone_number,
            additional_message=additional_message
        )