from django import forms
from .models import Post

class PostTweet(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'tweet_title',
            'tweet_text',
            'image',
        ]