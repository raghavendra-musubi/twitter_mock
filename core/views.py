from django.shortcuts import redirect, render
from .models import Post
from .forms import PostTweet, ReplyTweet


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
        # print(post_form)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post_form = PostTweet()

    context = {
        'form': post_form,
    }

    return render(request, 'core/post_tweet.html', context)

def reply(request, pk):

    parent_tweet = Post.objects.get(pk=pk)

    if request.method == 'POST':
        reply_form = ReplyTweet(request.POST)
        if reply_form.is_valid():
            reply_form.save()
            return redirect('detail', pk=pk)
    else:
        reply_form = ReplyTweet(initial={'parent_tweet_id': pk})

    context = {
        'parent_tweet': parent_tweet,
        'form': reply_form,
    }

    return render(request, 'core/reply.html', context)

def tweet_detail(request, pk):

    parent_tweet = Post.objects.get(pk=pk)
    reply_tweets = Post.objects.filter(parent_tweet_id=pk)

    context= {
        'parent_tweet': parent_tweet,
        'reply_tweets': reply_tweets,
    }

    return render(request, 'core/tweet_detail.html', context)
    