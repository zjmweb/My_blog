from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class basicinfo(models.Model):
    college = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    edubg = models.CharField(max_length=100)
    age = models.IntegerField()
    birthplace = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    wechat = models.CharField(max_length=100)

    def getcollege(self):
        return self.college

    def getage(self):
        return self.age

    def getemail(self):
        return self.email

class skills(models.Model):
    skills = models.CharField(max_length=100)

    def getskills(self):
        return self.skills

class interest(models.Model):
    interest = models.CharField(max_length=100)

    def getinterest(self):
        return self.interest

class eduexperience(models.Model):
    school = models.CharField(max_length=100)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
    major = models.CharField(max_length=100,default="school")
    description = models.TextField()

    def getschool(self):
        return self.school

    def getstart(self):
        return self.start

class certificate(models.Model):
    time = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def gettime(self):
        return self.time

    def getname(self):
        return self.name


class selfcomment(models.Model):
    comment = models.CharField(max_length=200)

    def getcomment(self):
        return self.comment

