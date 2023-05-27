from django import forms

class myform(forms.Form):
    name=forms.CharField(max_length=100)
    no=forms.IntegerField()