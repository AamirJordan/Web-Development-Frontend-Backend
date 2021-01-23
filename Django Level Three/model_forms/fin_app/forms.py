from django import forms
from fin_app.models import Enduser

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Enduser
        fields = "__all__"
