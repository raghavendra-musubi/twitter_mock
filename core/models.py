from django.db import models

# Create your models here.

class Post(models.Model):
    parent_tweet_id = models.PositiveIntegerField(null=True)
    tweet_title = models.CharField('Tweet Title',max_length=140, blank=False)
    tweet_text = models.CharField('Tweet Text',max_length=140, blank=False)    
    image = models.ImageField(upload_to='tweet_images/', blank=True )
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.tweet_title) + ': ' + str(self.parent_tweet_id)
