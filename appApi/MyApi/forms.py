from django import forms 
from .models import *




class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields=["user","content","image"]


    def clean_content(self,*args,**kwargs):
        content=self.cleaned_data["content"]
        if len(content) >10:
            raise forms.ValidationError("you must type less that 10 words")
        return super().clean(*args,**kwargs)