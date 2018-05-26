from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1',\
                                     'type': 'text', 'aria-describedby': 'emailHelp',\
                                      'placeholder': 'Enter username'}),
                                max_length=30,
                                required=True,
                                help_text='Usernames may contain <strong>alphanumeric</strong>,\
                                             <strong>_</strong> and <strong>.</strong> characters')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
       
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1',\
                                     'type': 'text', 'aria-describedby': 'emailHelp',\
                                      'placeholder': 'Enter username'}),
                                max_length=50,
                                required=True,
                                help_text='Usernames may contain <strong>alphanumeric</strong>,\
                                             <strong>_</strong> and <strong>.</strong> characters')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1',\
                                     'type': 'text', 'aria-describedby': 'emailHelp',\
                                      'placeholder': 'Email'}),
                                max_length=50,
                                required=True,
                                help_text='Usernames may contain <strong>alphanumeric</strong>,\
                                             <strong>_</strong> and <strong>.</strong> characters')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm_password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'confirm_password',
        ]

    

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password must match")
        return password
