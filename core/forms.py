from django import forms
from .models import Xodim


class XodimForm(forms.ModelForm):
    class Meta:
        model = Xodim
        fields = ['name', 'age', 'position', 'salary', 'city', 'department']
        labels = {
           
        }