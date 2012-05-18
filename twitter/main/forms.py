from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from main.models import Users, Auth, Tweet


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)


class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


def save(self, commit=True):
    user = super(UserCreateForm, self).save(commit=False)
    user.first_name = self.cleaned_data["first_name"]
    user.last_name = self.cleaned_data["last_name"]
    user.email = self.cleaned_data["email"]
    user.location = self.cleaned_data["location"]
    user.about_me = self.cleaned_data["about_me"]
    user.set.password(self.cleaned_data["password"])
    if commit:
        user.save()
    return user


class RegistrationForm(ModelForm):
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Users
        fields= ("location","about_me","name","birthday",)
        exclude = ('user','image',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
                User.objects.get(username=username)
        except User.DoesNotExist:
                return username
        raise forms.ValidationError("That username is already taken, please select another")

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
                raise forms.ValidationError("The passwords did not match. Please try again")
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('user','image',)

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet

