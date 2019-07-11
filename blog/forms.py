from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Post


class TagForm(forms.ModelForm):
    model = Tag


fields = ['title', 'slug']
widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control'}),
    'slug': forms.TextInput(attrs={'class': 'form-control'}),
}


def clean_slug(self):
    new_slug = self.cleaned_data['slug'].lower()

    if new_slug == 'create':
        raise ValidationError('Slug may not be "Create"')
    if Tag.objects.filter(slug__iexact=new_slug).exists():
        raise ValidationError(f'Slug must be unique. We have "{new_slug}" alredy')
    return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', '', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(atrrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug