from django import forms
from django_countries import countries   # ✅ import countries
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ✅ Convert the lazy BlankChoiceIterator to a concrete list
        if "default_country" in self.fields:
            self.fields["default_country"].choices = list(countries)

        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
        }

        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_country":
                placeholder = placeholders[field]
                if self.fields[field].required:
                    placeholder += " *"
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = (
                "border-black rounded-0 profile-form-input"
            )
            self.fields[field].label = False
