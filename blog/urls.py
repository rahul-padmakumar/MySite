from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartPageView.as_view(), name="starting_page"),
    path("posts", views.all_posts, name="posts_page"),
    path("posts/<slug:slug>", views.individual_post, name="posts_detail_page")
]
