from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=500)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to="posts", null=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tag = models.ManyToManyField(Tag)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.author.first_name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

