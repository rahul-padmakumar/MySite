from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=500)
    content = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    slug = models.SlugField()
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}, {self.author.first_name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

