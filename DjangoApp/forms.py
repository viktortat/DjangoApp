from django import forms

# https://djbook.ru/rel1.9/topics/forms/index.html
class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':80}),max_length=300)