from django.db import models
from django.utils import timezone

#Idea model
class Idea (models.Model):
    DOMAINS = (
        ('T', 'Tourism'),
        ('E', 'Education'),
        ('A', 'Agriculture'),
        ('C', 'Technology'),
        ('S', 'Service'),
    )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    about = models.TextField()
    domain = models.CharField(max_length=20, choices= DOMAINS)
    tags = models.CharField(max_length=100, blank= True)
    created_date = models.DateTimeField(
            default=timezone.now)
    dislikes = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)



