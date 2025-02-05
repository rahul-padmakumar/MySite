from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import date
from .models import Post
from django.views.generic import ListView, DeleteView
from django.views import View
from .forms import CommentForm
from django.urls import reverse

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

class POSTDetailView(View):

    def get_context(self, post, form):
        return {
            "identified_post": post,
            "tags": post.tag.all(),
            "form": form,
            "comments": post.comments.all().order_by("-id")
        }

    def get(self, req, slug):
        context = self.get_context(
            Post.objects.get(slug = slug),
            CommentForm()
        )
        return render(req, "blog/post_details.html", context)
    
    def post(self, req, slug):
        form = CommentForm(req.POST)
        post = Post.objects.get(slug = slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("posts_detail_page", args=[slug]))
        return render(req, "blog/post_details.html", self.get_context(post, form))
    

def get_date(post):
    return post['date']