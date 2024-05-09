from django import forms

from .models import Activity


class ActivityInputForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            'title',
            'date',
            'description',
            'file'
        ]
