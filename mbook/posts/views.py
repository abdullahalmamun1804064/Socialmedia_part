from django.shortcuts import redirect, render
from .models import Like, Post
from profiles.models import profile
from django.core.paginator import Paginator

def post_comment_create_add_view(request):
    post_qs=Post.objects.all()
    myprofile=profile.objects.get(user=request.user)
    p=Paginator(post_qs,1)
    page=request.GET.get('page')
    post_page=p.get_page(page)
    pg_nums= 'a' * post_page.paginator.num_pages

    dic={
       'post_qs':post_qs,
        'myprofile': myprofile,
        'post_page':post_page,
        'pg_nums':pg_nums,
        }
    return render (request,'posts/main.html',dic)



def like_unlike(request):
    user=request.user
    post_id=request.POST.get('post_id')
    print('---------id------------',post_id)
  
    post_i=request.POST['post_id']
    print('---------i------------',post_i)

    post_obj=Post.objects.get(id=post_id)
    #print('---------post_obj------------',post_obj)
    profil=profile.objects.get(user=user)
    #print('---------profile------------',profil)

    if profil in post_obj.liked.all():
       # print('---------Yes------------')
        post_obj.liked.remove(profil)
    else:
        #print('---------No------------')
        post_obj.liked.add(profil)


    like, create=Like.objects.get_or_create(user=profil,post_id=post_id)
    print(like)
    
    if not create:
        if like.value=='Unlike':
            like.value="Like"
        else :
            like.value="Unlike"
    else :
         like.value="Like"

    post_obj.save()
    like.save()



    return redirect('/post')