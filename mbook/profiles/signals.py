from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import profile,Relationship
from django.dispatch import receiver

@receiver(post_save,sender=User)
def post_save_create_profile (sender ,instance,created, **kwargs  ):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save,sender=Relationship)
def post_save_add_to_friend(sender,instance,created,**kwargs):

    sender_=instance.sender
    receiver_=instance.recever
    status_=instance.status
    if status_=='accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()