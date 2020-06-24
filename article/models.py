from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
# Create your models here.

class ArticleColumn(models.Model):
    title = models.CharField(max_length=100,blank=True)
    created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class ArticlePost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CharField,
        related_name='article'
    )

    body = models.TextField()
    tags = TaggableManager(blank=True)

    picture = models.ImageField(upload_to='article/%Y%m%d/', blank=True)  #deal with the picture when saving
    def save(self,*args,**kwargs):
        article = super(ArticlePost,self).save(*args,**kwargs)

        if self.picture and not kwargs.get('update_fields'):
            image = Image.open(self.picture)
            (x,y) = image.size
            new_x = 400
            new_y = int(new_x * (y/x))
            resized_image = image.resize((new_x,new_y),Image.ANTIALIAS)
            resized_image.save(self.picture.path)
        return article

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail',args=[self.id])

    def was_created_recently(self):
        diff = timezone.now() - self.created
        if diff.days <= 0 and diff.seconds < 60:
            return True
        else:
            return False
