from django import forms
from .models import Rewan2

class RewanForm(forms.ModelForm):
    class Meta:
        model = Rewan2
        fields = "__all__"