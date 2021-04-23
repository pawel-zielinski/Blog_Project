from django import forms
from .models import Blog, Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea, label='Comment:', required = False)
    class Meta:
        model = Comment
        fields = ('comment',)
