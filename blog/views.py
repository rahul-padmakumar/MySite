from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Post

# Create your views here.

def get_date(post):
    return post['date']


def start_page(req):
    posts = Post.objects.all().order_by("-date")[:3]
    return render(req, "blog/start_page.html", {"latest_posts":posts})

def all_posts(req):
    posts = Post.objects.all().order_by("-date")
    return render(req, "blog/all_posts.html", {"all_posts": posts})

def individual_post(req, slug):
    post = Post.objects.get(slug = slug)
    tags = post.tag.all()
    print(post)
    return render(req, "blog/post_details.html", {"identified_post": post, "tags": tags})
