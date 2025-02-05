from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Post
from django.views.generic import ListView

# Create your views here.

class StartPageView(ListView):
    template_name = "blog/start_page.html"
    model = Post
    context_object_name = "latest_posts"
    ordering = "-date"
    def get_queryset(self):
        query = super().get_queryset()
        data = query[:3]
        return data
    
class AllPostView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = "-date"

def get_date(post):
    return post['date']

def individual_post(req, slug):
    post = Post.objects.get(slug = slug)
    tags = post.tag.all()
    print(post)
    return render(req, "blog/post_details.html", {"identified_post": post, "tags": tags})
