from django import forms
from .models import discussion, Categorys, Comment


cats = Categorys.objects.all().values_list('name', 'name')
cats_list = []
for cat in cats:
    cats_list.append(cat)


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = discussion
        fields = ('title', 'author', 'categorys', 'featured_image', 'excerpt', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden', 'value': '', 'id': 'author'}),
            'categorys': forms.Select(choices=cats_list, attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden', 'value': '', 'id': 'name'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }