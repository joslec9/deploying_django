from __future__ import unicode_literals

from django.db import models
import re, bcrypt
#
class UserManager(models.Manager):
    def create_user(self, data):
        print data
        errors = []
        if len(data['first_name']) < 2:
            errors.append('Please enter a valid first name')
        if len(data['last_name']) < 2:
            errors.append('Please enter a valid last name')
        if re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', data['email']):
            pass
        else:
            errors.append('Please enter a valid email address')
        if not data['password'] == data['confirm_password']:
            errors.append('Password fields do not match')
        elif len(data['password']) < 8:
            errors.append('Password must be at least 8 characters')
        else:
            password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
        if not errors:
            new_user = User.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=password)

            return (True, new_user)
        else:
            return (False, errors)
    def login_user(self, data):
        errors = []
        email = data['email']
        user = User.objects.filter(email=email)

        if user:
            if bcrypt.hashpw(data['password'].encode(),user[0].password.encode()) == user[0].password:
                print "Match"
            else:
                errors.append("Invalid Password")
        else:
            errors.append("Email does not match a user in the system")
        if not errors:
            return (True, user[0])
        else:
            return (False, errors)
class User(models.Model):
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    date_of_birth = models.DateTimeField(null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
