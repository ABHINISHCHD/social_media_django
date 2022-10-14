from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from flask import request_started
from .forms import profile_create,registration,posting_post,user_update,profile_update,login_form,comment
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import *
@login_required
def default(request):
    posts=posting.objects.all().order_by('id')
    paginator=Paginator(posts,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    login=profile.objects.get(user=request.user)
    to_follow=follow.objects.filter(follower=request.user)
    list_following=[]
    for i in to_follow:
        list_following.append(i.user)
    list_following.append(login.name)
    to_follow=profile.objects.all().exclude(name__in=list_following)

    context={
        "posts":page_obj,
        "login":login,     
        "accounts":to_follow     
    }
    
    return render(request,'default.html',context)


def register(request):
    if request.method=="POST":
        form1=registration(request.POST)
        form2=profile_create(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            obj=User.objects.get(username=form1.cleaned_data['username'])
            form2.instance.user=obj
            form2.instance.name=form1.cleaned_data['username']
            form2.save()
            return render(request,'default.html')
        else:
            form1=registration()
            form2=profile_create()
            context={
            "register":form1,
            "profile":form2
                      
            }
            return render(request,'register.html',context) 
           
    else:
        form1=registration()
        form2=profile_create()
        context={
            "register":form1,
            "profile":form2
                      
            }
        return render(request,'register.html',context) 

@login_required
def post(request):
    
    if request.method=="POST":
        form=posting_post(request.POST,request.FILES)
        obj=profile.objects.get(user=request.user)
        form.instance.person=obj
        if form.is_valid():
            form.save()
            return redirect('dashboard:home')
        print(form.errors.as_data())
        return HttpResponse('something wrong')


    else:
        login=profile.objects.get(user=request.user)
        post_form=posting_post()
        context={
            "post":post_form,
            "login":login     

        }
        return render(request,'posting.html',context)


def update(request):
    if request.method=='POST':
        person=profile.objects.get(user=request.user)
        form1=user_update(request.POST,instance=request.user)
        form2=profile_update(request.POST,request.FILES,instance=person)
        if form1.is_valid and form2.is_valid:
            form1.save()
            form2.save()
            return redirect('dashboard:update')
    else:
        person=profile.objects.get(user=request.user)
        form1=user_update(instance=request.user)
        form2=profile_update(instance=person)
        login=profile.objects.get(user=request.user)

        context={
            'form1':form1,
            'form2':form2,
            'login':login
        }
        return render(request,'profile.html',context)


def loginpage(request):
    if request.method=="POST":
        name=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard:home')
        else:
            form=login_form()
            return render(request,'login.html',{'form':form})    

    else:
        form=login_form()
        return render(request,'login.html',{'form':form})

def logoutPage(request):
    logout(request)
    return redirect('dashboard:login')

def profile_info(request,pk):
    person=profile.objects.get(user=pk)
    posts=posting.objects.filter(person=person)
    no_post=len(posts)
    login=profile.objects.get(name=request.user.username)
    followers=request.user.username
    user=person.name
    if follow.objects.filter(follower=followers,user=user).first():
        btn_text='Unfollow'
    else:
        btn_text='Follow'
    follower=len(follow.objects.filter(user=person.name))
    following=len(follow.objects.filter(follower=person.name))

    context={
        'person':person,
        'posts':posts,
        'no_post':no_post,
        'btn_text':btn_text,
        'follower':follower,
        'following':following,
        'login':login
         }
    return render(request,'person_info.html',context)

def follow_count(request):
    if request.method=='POST':
        follower=request.POST.get('follower')
        user=request.POST.get('user')
        print(user)
        obj=profile.objects.get(name=user)  
        if follow.objects.filter(follower=follower,user=user).first():
            delete_user=follow.objects.get(follower=follower,user=user)
            delete_user.delete()
            return redirect("/",pk=obj.user.id)
        else:
            new_follower=follow.objects.create(follower=follower,user=user)
            new_follower.save()
            return redirect("/",pk=obj.user.id)
    else:
        return redirect("/")

def like_post(request):
    username=request.user.username
    post_id=request.GET.get('post_id')
    post=posting.objects.get(id=post_id)
    like_filter=like.objects.filter(post_id=post_id,username=username).first()

    if like_filter==None:
        new_like=like.objects.create(post_id=post_id,username=username)
        new_like.save()
        post.likes=post.likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.likes=post.likes-1
        post.save()
        return redirect('/')


def comment_input(request):
    if request.method == 'POST':
        post_id=request.POST.get('post_id')
        comm=comment(request.POST)
        comm.instance.post_id=post_id
        comm.instance.person=request.user
        if comm.is_valid():
            comm.save()
            return redirect('/')
        
        
    else:
        comm=comment()
        context={
            'comment':comm
        }
        return render(request,'comment.html',context)


def show_comment(request):
    post_id=request.POST.get('post_id')
    comm=comment.objects.filter(post_id=post_id)
    context={
        'comment':comm
    }
    return redirect('/')


class account_list(ListAPIView):
    queryset=profile.objects.all()
    serializer_class=account
class account_retrive(RetrieveAPIView):
    queryset=profile.objects.all()
    serializer_class=account
