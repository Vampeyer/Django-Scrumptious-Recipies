from django import forms
class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget = forms.PasswordInput,
    )
    password_confirmation = forms.CharField(
        max_length = 150,
        widget = forms.PasswordInput,
    )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,)
