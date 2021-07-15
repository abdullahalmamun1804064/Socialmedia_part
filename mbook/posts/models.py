import re
from django.db import models
from profiles.models import profile
from django.core.validators import FileExtensionValidator

class Post(models.Model):
    content=models.TextField()
    author=models.ForeignKey(profile,on_delete=models.CASCADE,related_name="posts")
    image=models.ImageField(upload_to='posts',validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True)
    liked=models.ManyToManyField(profile,blank=True,related_name='likes')
    updates=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:20]}"
    def num_like(self):
        return f"{self.liked.all().count()}"
  
    def number_of_comment(self):
        return f"{self.Comment_set.all().count()}"

    class Meta:
        ordering=['-created']

class Comment (models.Model):
    user=models.ForeignKey(profile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField()
    updates=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.body}'

LIKES_CHOICES=(
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like (models.Model):
    user=models.ForeignKey(profile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    value=models.CharField(max_length=10,choices=LIKES_CHOICES)
    updates=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.post} - {self.value}'
    
    
    