from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all # 쿼리셋 # 메소드
    total = Post.objects.count
    return render(request,'home.html',{'posts_list':posts,'total':total})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form=PostForm()
    return render(request,'new.html',{'form':form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post':post})

def post_edit(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'post_edit.html',{'form':form})

def post_remove(request, pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('home')