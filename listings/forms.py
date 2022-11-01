from dataclasses import fields
from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "description",
            "price",
            "num_bedrooms",
            "num_bathrooms",
            "square_footage",
            "address",
            "image",
            "is_featured",
        ]