import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .models import Blog


def index(request):
    latest_blog_list = Blog.objects.all().order_by('-post_date')[:10]
    context = {
        'latest_blog_list':latest_blog_list,
    }
    return render(request, 'index.html', context)


def readBlog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comment_set.all()
    context = {
        'blog':blog,
        'comments':comments,
    }
    return render(request, 'readBlog.html', context)


def comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comment_set.all()
    context = {
        'comments':comments,
        'blog':blog,
    }

    return render(request, 'comment.html', context)


def writeBlog(request):
    return render(request, 'blogEntry.html')

def postEntry(request):
    b = Blog()
    b.title= request.POST['title']
    b.reply_to = request.POST['reply_to']
    b.author = request.POST['author']
    b.img = request.POST['img']
    b.content = request.POST['content']
    b.post_date = datetime.datetime.now()
    b.save()
    return redirect('/')


def addComment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog':blog,
    }
    return render(request, 'addComment.html', context)

def postComment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    content = request.POST['content']
    rating = request.POST['rating']

    comment = blog.comment_set.create(content=content, rating=rating)
    comment.save()

    return redirect('/')
