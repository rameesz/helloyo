# fruits/forms.py
from django import forms
from .models import FruitSet

class FruitSetForm(forms.ModelForm):
    class Meta:
        model = FruitSet
        fields = ['fruit1', 'fruit2', 'fruit3', 'fruit4', 'fruit5', 'result']
