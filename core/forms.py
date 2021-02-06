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

class ReplyTweet(forms.ModelForm):
    class Meta:
        model = Post 
        fields = [
            'parent_tweet_id',
            'tweet_title',
            'tweet_text',
        ]
        widgets = {'parent_tweet_id': forms.HiddenInput()}
        