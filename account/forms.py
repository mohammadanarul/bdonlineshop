from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = UserCreationForm.Meta.fields

class user_register_form(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Require. Add a valid email address.")
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

        def clean_email(self):
            email = self.cleaned_data["email"].lower()
            try:
                account = Account.objects.get(email=email)
            except Exception as e:
                return email
            raise forms.ValidationError(f'Email {account} is Alredy in use.')
        
        def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                account = Account.objects.get(username=username)
            except Exception as e:
                return username
            raise forms.ValidationError(f'Username {account} is Alredy in use.')