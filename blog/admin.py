from django.contrib import admin

# Register your models here.
from .models import Post, Tag, Author

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
