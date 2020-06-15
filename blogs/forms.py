from django import forms
from .models import Resource


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)



class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields = ['title','pdf']