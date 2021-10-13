from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteOwners(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    so_email = models.CharField(max_length=100, null=True)
    so_social_handle = models.CharField(max_length=100, null=True)
    os_home_address = models.CharField(max_length=100, null=False)

class SiteUsers(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=True)
    social_handle = models.CharField(max_length=100, null=True)
    home_address = models.CharField(max_length=100, null=False)

class Question(models.Model):
    author = models.ForeignKey(User, null=False, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    
    def get_responses(self):
        return self.responses.filter(parent=None)

class Response(models.Model):
    user = models.ForeignKey(User, null=False, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete = models.CASCADE, related_name = 'responses')
    parent = models.ForeignKey('self', null=True, blank = True, on_delete = models.CASCADE)
    body = models.TextField(null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.body
    
    def get_responses(self):
        return Response.object.filter(parent=self)