from django import forms
from django.contrib.auth import(
        authenticate,
        get_user_model,
        login,
        logout,
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        #user_qs = User.objects.filter(username=username)
        #if user_qs.count()==1:
            #user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("user is not logged in")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')
    confirm_email = forms.EmailField(label='Confirm Email Address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'confirm_email', 'password']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        confirm_email = self.cleaned_data.get('confirm_email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email address is already registered")
        if email != confirm_email:
            raise forms.ValidationError("Emails do not match")
        return super(UserRegisterForm, self).clean(*args, **kwargs)