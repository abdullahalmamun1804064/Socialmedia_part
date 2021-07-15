from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import get_random_code

# Create your models here.
class profile(models.Model):
    frist_name=models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    bio =models.TextField(max_length=200,blank=True,default='No Bio.....')
    email =models.EmailField(blank=True, max_length=254)
    country =models.CharField(max_length=200,blank=True)
    avatar =models.ImageField(default='avaters/avatars.jpg',upload_to='avaters')
    friends =models.ManyToManyField(User,related_name='friends',blank=True)
    slug =models.SlugField(unique=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def get_all_friends(self):
        return self.friends.all()
    def get_all_friends_count(self):
        return self.friends.all().count()
    def get_post_number(self):
        return self.posts.all().count()
    
    def get_all_author_post(self):
        return self.posts.all()
    
    def get_like_given_no(self):
        likes=self.like_set.all()
        total_liked=0
        for item in likes :
           if item.value=='Like':
               total_liked +=1
        return total_liked
    
    def get_like_recieved_no(self):
        posts=self.posts.all()
        total_liked=0
        for item in posts :
            total_liked +=item.liked.all().count()
        return total_liked



    def __str__(self) :
        return f"{self.user.username} {self.created.strftime('%d-%m-%y')}"
    
    def save (self,*args, **kwargs):
        ex=False
        if self.frist_name and self.last_name:
            to_slug=slugify(str(self.frist_name)+" "+str(self.last_name))
            ex=profile.objects.filter(slug=to_slug).exists()

            while ex:
                to_slug=slugify(to_slug+" "+str(get_random_code()))
                ex=profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug=str(self.user)
        self.slug=to_slug
        super().save(*args,**kwargs)


STSTUS=(
    ('send','send'),
    ('accepted','accepted'),
)

class Relationship(models.Model):
    sender=models.ForeignKey(profile,on_delete=models.CASCADE,related_name='sender' )
    recever=models.ForeignKey(profile,on_delete=models.CASCADE,related_name='recever' )
    status=models.CharField(choices=STSTUS,max_length=8)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.recever}"


    

