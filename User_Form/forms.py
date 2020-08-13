from django import forms


class UsrForm(forms.Form):
    ustitle=forms.CharField(max_length=50,
    widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder': 'name',
        'id':'inputname'
    }))


    usdescription=forms.CharField(max_length=50,
    widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder': 'Comment',
        'rows':'5',
        'id':'comment'


    }))
