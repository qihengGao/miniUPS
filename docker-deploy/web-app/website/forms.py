from re import A
from django import forms
from website.models import Package


class RegisterForm(forms.Form):
    username = forms.CharField(label='Your username', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.CharField(label='Your Email', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Your Password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat your password', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your user name'}))

    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter password'}))


class TrackForm(forms.Form):
    trackingid = forms.IntegerField(label='What are you looking for', required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Tracking Number'}))

    # def clean_trackingid(self):
    #     trackingid = self.cleaned_data.get('trakingid')
    #     filter_result = Package.objects.filter(tracking_id=trackingid)
    #     if len(filter_result) <= 0:
    #         raise forms.ValidationError(
    #             "The tracking number you entered is not valid.")


class DestAddrForm(forms.Form):
    x = forms.IntegerField(label='x', required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'x'}))
    y = forms.IntegerField(label='y', required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'y'}))
