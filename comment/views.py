from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Comment

from article.models import ArticlePost
from .forms import CommentForm
from notifications.signals import notify
from django.contrib.auth.models import User

# Create your views here.

# post comment on current article
@login_required(login_url='/userprofile/login/')
def post_comment(request,article_id,parent_comment_id=None):
    article = get_object_or_404(ArticlePost,id=article_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            # secondary
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                # if surpass secondary,then turn into secondary
                new_comment.parent_id = parent_comment.get_root().id
                # person who was replyed
                new_comment.reply_to = parent_comment.user
                new_comment.save()

                # if not parent_comment.user.is_superuser:
                notify.send(
                    request.user,
                    recipient=parent_comment.user,
                    verb='Reply to you',
                    target=article,
                    action_object=new_comment,
                    )

                return HttpResponse('200 OK')

            new_comment.save()
            # superuser
            if not request.user.is_superuser:
                notify.send(
                    request.user,
                    recipient=User.objects.filter(is_superuser=1),
                    verb='Reply to you',
                    target=article,
                    action_object=new_comment,
                )

            return redirect(article)
        else:
            return HttpResponse("The content of form is wrong!Please fill in the form again.")

    elif request.method == 'GET':
        comment_form = CommentForm()
        context = {
            'comment_form':comment_form,
            'article_id':article_id,
            'parent_comment_id':parent_comment_id
        }
        return render(request,'comment/reply.html',context)
    else:
        return HttpResponse("The function comment only accept Post request.")


@login_required(login_url='/userprofile/login/')
def delete_comment(request,id):

    comment = Comment.objects.get(id=id)

    article = get_object_or_404(ArticlePost, id=comment.article.id)

    user = comment.user

    if request.user != user:
        return HttpResponse("You do not have the right to delete the comment.")
    else :
        comment.delete()
        return redirect(article)