from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
                label='Name', 
                max_length=100,
                widget=forms.TextInput(attrs={'autocomplete':'off'}))
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)