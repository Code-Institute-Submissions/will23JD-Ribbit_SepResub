from django import forms
from .models import discussion

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = discussion
        fields = ('title', 'slug', 'author', 'featured_image', 'excerpt', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'slug': ('title',)}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
