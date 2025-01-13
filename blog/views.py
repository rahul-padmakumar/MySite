from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def start_page(req):
    return HttpResponse("I am starting page")

def all_posts(req):
    return HttpResponse("All Posts")

def individual_post(req, post_name):
    return HttpResponse(f"Post name is: {post_name}")
