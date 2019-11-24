from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['txt', 'done']
        widgets = {
            'txt': forms.TextInput(attrs=
            {
                'placeholder': 'What\'s your next task ...',
                'class' : 'form-control',
                'autocomplete': 'off'
            },
            )
        }