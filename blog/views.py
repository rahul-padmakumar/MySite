from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Post
from django.views.generic import ListView, DeleteView
from .forms import CommentForm

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

class POSTDetailView(DeleteView):
    template_name = "blog/post_details.html"
    model = Post
    context_object_name="identified_post"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.get_object().tag.all()
        context["form"] = CommentForm()
        return context
    

def get_date(post):
    return post['date']