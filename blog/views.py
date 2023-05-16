from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def frontpage(request):
    posts = Post.objects.all()


    context = {'posts':posts, }
    return render(request, 'blog/frontpage.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)           # we cannot save directly to database coz its a forigen key.
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
        
    else:
        form = CommentForm()

    context = {'post':post, 'form':form}
    return render(request, 'blog/post_detail.html', context)

