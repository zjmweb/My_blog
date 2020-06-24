from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import UserLogin,UserRegister
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile


# Create your views here.
def user_login(request):
    if request.method == "POST":
        user_login_form = UserLogin(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'],password=data['password'])
            if user:
                login(request,user)
                return redirect("article:article_list")
            else:
                return HttpResponse("Error:Username or password is wrong,please input again!")

        else:
            return HttpResponse("Error:Username or password disobeys the principle!")

    elif request.method == "GET":
        user_login_form = UserLogin()
        context = { 'form': user_login_form}
        return render(request,'userprofile/login.html',context)
    else:
        return HttpResponse("Please use Get or Post to request data!")


def user_logout(request):
    logout(request)
    return redirect("article:article_list")

def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegister(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)

            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()

            login(request,new_user)
            return redirect("article:article_list")
        else:
            return HttpResponse("Error:Register Form is wrong. Please input again!")

    elif request.method == 'GET':
        user_register_form = UserRegister()
        context = { 'form': user_register_form }
        return render(request,'userprofile/register.html',context)
    else:
        return HttpResponse("Please use GET or Post to request data!")


@login_required(login_url='/userprofile/login/')
def user_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        if request.user == user:

            logout(request)
            user.delete()
            return redirect("article:article_list")
        else:
            return HttpResponse("You do not have the right to delete")
    else:
        return HttpResponse("Only accept post request.")


@login_required(login_url='/userprofile/login/')
def profile_edit(request,id):
    user = User.objects.get(id=id)
    if Profile.objects.filter(user_id=id).exists():
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("You do not have the right to edit the user profile!")

        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            if 'portrait' in request.FILES:
                profile.portrait = profile_cd["portrait"]
            profile.save()

            return redirect("userprofile:edit",id=id)
        else:
            return HttpResponse("The registered form is wrong! Please input again!")

    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = { 'profile_form': profile_form,'profile':profile,'user':user}
        return render(request,'userprofile/edit.html',context)
    else:
        return HttpResponse("Please use GET OR POST to request data.")
