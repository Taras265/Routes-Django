from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'Імя'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Пароль'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise ValueError('Нема пользователя з таким ніком')
            if not check_password(password, qs[0].password):
                raise ValueError('Пароль не вірен')
            user = authenticate(username=username, password=password)
            if not user:
                raise ValueError('Пользователь неактивен')
            return super().clean(*args, **kwargs)
