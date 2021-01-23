from django import forms


class zodiac(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
