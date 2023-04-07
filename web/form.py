from django import forms
from .models import Post_job

class Post_jobForm(forms.ModelForm):
    class  Meta:
        model=Post_job
        fields=("company_name","company_logo")