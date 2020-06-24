from django.contrib import admin
# Register your models here.
from .models import basicinfo,skills,interest,eduexperience,certificate,selfcomment

admin.site.register(basicinfo)
admin.site.register(skills)
admin.site.register(interest)
admin.site.register(eduexperience)
admin.site.register(certificate)
admin.site.register(selfcomment)