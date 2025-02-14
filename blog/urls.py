from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartPageView.as_view(), name="starting_page"),
    path("posts", views.AllPostView.as_view(), name="posts_page"),
    path("posts/<slug:slug>", views.POSTDetailView.as_view(), name="posts_detail_page"),
    path("read_later", views.ReadLaterView.as_view(), name="read_later")
]
