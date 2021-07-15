from django import forms
from .models import profile

class profile_forms(forms.ModelForm):
    class Meta:
        model=profile
        fields=('frist_name','last_name','bio','avatar')
        widgets={
            'frist_name':forms.TextInput(attrs={"class":'form-control'}),
            'last_name':forms.TextInput(attrs={"class":'form-control'}),
            'bio':forms.Textarea(attrs={"class":'form-control'}),
            'avatar':forms.ClearableFileInput(attrs={"class":'form-control'}),



           }

