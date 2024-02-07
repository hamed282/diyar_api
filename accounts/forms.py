from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from django.core.exceptions import ValidationError


from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'national_code', 'email', 'city']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dont match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you can change password using <a href=\"../password/\" >'
                                                   'this form <a/>.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'national_code', 'city', 'email', 'is_active', 'is_admin',
                  'is_superuser', 'last_login']


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    national_code = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)


class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
