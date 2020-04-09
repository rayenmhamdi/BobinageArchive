from django import forms
from .models import Archive

class ArchiveCreateForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = '__all__'