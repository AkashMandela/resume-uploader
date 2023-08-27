from django import forms
from .models import Form


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Form
        fields = ('name', 'cv','file','image','exp')