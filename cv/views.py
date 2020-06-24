from django.shortcuts import render
from django.http import HttpResponse
from .models import basicinfo,skills,interest,eduexperience,certificate,selfcomment

# Create your views here.


def cv(request):
    infos = basicinfo.objects.get(id=1)
    skill_list = skills.objects.all()
    interest_list = interest.objects.all()
    eduex_list = eduexperience.objects.all()
    cert_list = certificate.objects.all()
    comment_list = selfcomment.objects.all()
    context = { 'infos': infos, 'skill_list':skill_list, 'interest_list':interest_list,
                'eduex_list':eduex_list, 'cert_list':cert_list, 'comment_list':comment_list}
    print(infos.college)
    return render(request,'cv.html',context)

