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

    def is_saved_posts(self, req, post_id):
        saved_post_ids = req.session.get("saved_posts")
        print(type(post_id))
        print(type(saved_post_ids))
        if saved_post_ids is not None:
            return post_id in saved_post_ids
        else:
            return False

    def get_context(self, post, form, req):
        return {
            "identified_post": post,
            "tags": post.tag.all(),
            "form": form,
            "comments": post.comments.all().order_by("-id"),
            "is_saved_post": self.is_saved_posts(req, post.id)
        }

    def get(self, req, slug):
        context = self.get_context(
            Post.objects.get(slug = slug),
            CommentForm(),
            req=req
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
        return render(req, "blog/post_details.html", self.get_context(post, form, req))
    

class ReadLaterView(View):
    def get(self, req):
        saved_post_ids = req.session.get("saved_posts")
        if saved_post_ids is None or len(saved_post_ids) == 0:
            saved_posts = []
            has_saved_post = False
        else:
            saved_posts = Post.objects.filter(id__in=saved_post_ids)
            has_saved_post = True
        print(saved_posts)
        return render(req, "blog/read_later.html", {"saved_posts":saved_posts, "has_saved_posts": has_saved_post})        

    def post(self, req):
        post_id = int(req.POST["post_id"])
        saved_post_ids = req.session.get("saved_posts")

        if saved_post_ids is None:
            saved_post_ids = []

        for id in saved_post_ids:
            print(type(id))

        if post_id in saved_post_ids:
            saved_post_ids.remove(post_id)
        else:
            saved_post_ids.append(post_id)

        req.session["saved_posts"] = saved_post_ids
        return HttpResponseRedirect("/")
    

def get_date(post):
    return post['date']