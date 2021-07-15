from django.urls import path
from . import views

apps_name='posts'

urlpatterns = [
      path('', views.post_comment_create_add_view,name='post'),
      path('like_unlike', views.like_unlike,name='like_unlike'),

  
]
