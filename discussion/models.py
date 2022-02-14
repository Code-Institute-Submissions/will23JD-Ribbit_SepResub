from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Discussion model
class discussion(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ribbit_discussion")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='discussion_likes', blank=True)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
