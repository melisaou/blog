from django import forms
from blog.models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = {'comment'}
        widgets = {
            'comment':forms.Textarea(attrs={'class':'form-control'})
        }