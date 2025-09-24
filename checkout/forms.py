from django import forms
from django_countries import countries
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name", "email", "phone_number",
            "street_address1", "street_address2",
            "town_or_city", "postcode", "country", "county",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ✅ Completely bypass the lazy BlankChoiceIterator
        self.fields["country"].choices = list(countries)  # real list of (code, name)

        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County, State or Locality",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                ph = placeholders[field]
                if self.fields[field].required:
                    ph += " *"
                self.fields[field].widget.attrs["placeholder"] = ph
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
