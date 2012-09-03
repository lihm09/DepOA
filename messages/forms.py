# encoding=utf-8

from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    title = forms.CharField(required=True,label='标题',
        widget=forms.TextInput(attrs={'size':30,'max_length':30}))
    content = forms.CharField(required=True,label='内容',widget=forms.Textarea(attrs={'size':10000}))


