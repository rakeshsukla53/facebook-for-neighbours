from django import forms
from django.contrib.auth import models
from register.models import Registration, Thread, Message
from django.forms import widgets
from django import forms


class UserModelForm(forms.ModelForm):
    # upassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = ['uname', 'upassword', 'uphone', 'uemail', 'uintro', 'uphoto', 'uaddress']
        labels = {
            'uname': 'Name',
            'upassword': 'Password',
            'uphone': 'Phone',
            'uemail': 'Email',
            'uintro': 'Intro',
            'uphoto': 'Display Picture',
            'uaddress': 'Address'
        }
        widgets = {
        'upassword': forms.PasswordInput(),
        }

class ThreadModelForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = '__all__'
        exclude = ['tauthor', 'tid']
        labels = {
            'ttype': 'Type of Thread',
            'tdesc': 'Thread Description',
        }

class MessageModelForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['mauthor', 'tid']
        labels = {
            'mtext': 'Message',
        }
