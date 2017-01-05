from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'courses'
class Comments(models.Model):
    comment = models.CharField(max_length= 500)
    course = models.ForeignKey(Courses)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
class CourseUsers(models.Model):
    course = models.ForeignKey(Courses)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
