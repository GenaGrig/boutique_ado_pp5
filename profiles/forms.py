from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    This class allows us to create a form for the user to fill in
    their details when placing an order.
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        # The dictionary below maps the field names to their placeholders
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # The below loop iterates through the form fields and
        # sets a "*" as the placeholder for the field if it
        # is required, and sets the placeholder to the
        # corresponding value from the placeholders dictionary
        # if it is not required.
        # It also adds the class "stripe-style-input" to each
        # field, and removes the form field labels.
        # Finally, it sets the autofocus attribute on the
        # full name field.

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False

            self.fields['default_phone_number'].widget.attrs['autofocus'] = True
