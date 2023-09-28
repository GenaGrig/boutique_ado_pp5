from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    This class allows us to create a form for the user to fill in
    their details when placing an order.
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'country', 'postcode', 'town_or_city',
                  'street_address1', 'street_address2',
                  'county',)
        # The exclude attribute allows us to exclude fields from the form
        exclude = ('order_number', 'date', 'grand_total',
                   'delivery_cost', 'order_total',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        # The dictionary below maps the field names to their placeholders
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
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
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

            self.fields['full_name'].widget.attrs['autofocus'] = True
