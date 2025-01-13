from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def start_page(req):
    return render(req, "blog/start_page.html")

def all_posts(req):
    return render(req, "blog/all_posts.html")

def individual_post(req, post_name):
    return HttpResponse(f"Post name is: {post_name}")
