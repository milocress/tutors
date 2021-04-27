from django import forms

class SessionForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)

