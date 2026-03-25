from django import forms

# Went you use this class in your html you crate a inputs for every component
class CreateNewShop(forms.Form):
    name = forms.CharField( label='Name: ', max_length=30)