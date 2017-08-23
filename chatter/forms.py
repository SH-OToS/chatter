"""This is a program for use forms"""
from django import forms

class Name(forms.Form):
    """get chat info"""
    name = forms.CharField(
        label="name",
        max_length="20",
        required="True",
        widget=forms.TextInput()
    )

    text = forms.CharField(
        label="text",
        max_length="128",
        required="True",
        widget=forms.TextInput()
    )
