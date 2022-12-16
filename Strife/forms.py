from django import forms


class InputForm(forms.Form):
    username = forms.CharField(max_length=255,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label='')
