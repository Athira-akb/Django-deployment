from django import forms
from .import models
from django import forms

class user_form(forms.ModelForm):
    class Meta():
        model = models.user_model
        fields = '__all__'



