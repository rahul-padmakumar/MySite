from django.contrib import admin

# Register your models here.
from .models import Post, Tag, Author, CommentModel

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author","date", "tag")
    list_display = ("title", "date", "author")


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ("user_name", "comment_text",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(CommentModel, CommentModelAdmin)
