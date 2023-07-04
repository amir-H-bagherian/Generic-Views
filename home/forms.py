from django import forms
from .models import Student


class ContactForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()
    
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if 'hello' in content:
            return content
        else:
            raise forms.ValidationError('Say Hello!')