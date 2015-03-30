#__author__ = 'yangliu'
from django import forms


class ContactForms(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(label='e-mail')
    content = forms.CharField(widget=forms.Textarea)

    def clean_content(self):
        content = self.cleaned_data['content']
        length = len(content)

        if length < 4:
            raise forms.ValidationError('the words at least 4')

        return content
