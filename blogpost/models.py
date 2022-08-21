from django.db import models
from taggit.managers import TaggableManager
from tinymce import models as tinymce_models
from django.urls import reverse
import readtime


#Category
class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

#Blog posts.
class Post(models.Model):
    title = models.CharField(max_length= 200, null=True)
    categories = models.ManyToManyField(Category),
    overview = models.TextField(max_length= 500, null=True)
    content = tinymce_models.HTMLField('Content')
    thumbnail = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add= True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    #get the read duration of each blog post
    def get_readtime(self):
        result = readtime.of_text(self.content)
        return f'{result.text} read'

    def get_absolute_url(self):
        return reverse('blog:blog-details', kwargs={
            'id': self.id,
            'title': self.title,
        })

#Comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name= 'comments', null=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    objects = models.Manager()

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'comment by {self.name}'

#Comment Reply
class response_to_comment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name= 'response')
    name = models.CharField(max_length=50)
    response = models.TextField()

    def __str__(self):
        return f'response by {self.name}'

    
