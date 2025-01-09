from django import forms
from django.utils import timezone
from .models import SimpleTask

class TaskUpdateForm(forms.ModelForm):
    due_date = forms.DateField(required=False, input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    class Meta:
        model = SimpleTask
        fields = ['title', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
        labels = {
            'title': '',
            'due_date': '',
        }
        
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date == "":
            return None
        elif due_date and due_date < timezone.now().date():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date
    
class TaskCreateForm(forms.ModelForm):
    due_date = forms.DateField(required=False, input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    class Meta:
        model = SimpleTask
        fields = ['title', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date == "":
            return None
        elif due_date and due_date < timezone.now().date():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date
    