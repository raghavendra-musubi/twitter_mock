from django.shortcuts import redirect, render
from .models import Post
from .forms import PostTweet


# Create your views here.

def index(request):

    parent_tweets = Post.objects.filter(parent_tweet_id__isnull=True)

    context = {
        'parent_tweets': parent_tweets,
    }

    return render(request,'core/index.html', context)

def post_tweet(request):

    if request.method == 'POST':
        post_form = PostTweet(request.POST, request.FILES)
        print(post_form)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post_form = PostTweet()

    context = {
        'form': post_form,
    }

    return render(request, 'core/post_tweet.html', context)