from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.hashers import make_password


class InputForm(forms.Form):
    username = forms.CharField(max_length=255,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label='')


class RegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=255,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
                               label='')
    word1 = forms.CharField(max_length=255,
                            widget=forms.PasswordInput(attrs={'placeholder': 'Secure Word 1'}),
                            label='')
    word2 = forms.CharField(max_length=255,
                            widget=forms.PasswordInput(attrs={'placeholder': 'Secure Word 2'}),
                            label='')
    word3 = forms.CharField(max_length=255,
                            widget=forms.PasswordInput(attrs={'placeholder': 'Secure Word 3'}),
                            label='')

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'word1',
            'word2',
            'word3',
        ]

    def save(self, **kwargs):
        word1 = make_password(password=self.word1)
        word2 = make_password(password=self.word2)
        word3 = make_password(password=self.word3)

        super().save(**kwargs)


class TwoFactorAuthenticationForm(forms.Form):
    word1 = forms.CharField(max_length=255,
                            widget=forms.PasswordInput(attrs={'placeholder': 'Secure Word 1'}),
                            label='')
    word2 = forms.CharField(max_length=255,
                            widget=forms.PasswordInput(attrs={'placeholder': 'Secure Word 2'}),
                            label='')
    word3 = forms.CharField(max_length=255,
                            widget=forms.PasswordInput(attrs={'placeholder': 'Secure Word 3'}),
                            label='')
