from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from .models import ArticlePost
import markdown
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from comment.models import Comment
from .models import ArticleColumn
from comment.forms import CommentForm

# Create your views here.
def article_list(request):        # display articles according to search,column,order
    search = request.GET.get('search')
    order = request.GET.get('order')
    columns = ArticleColumn.objects.all()  # for header to display columns(columns can only be created in admin)
    column = request.GET.get('column')
    columnid = ArticleColumn.objects.filter(title=column).first()

    tag = request.GET.get('tag')

    article_list = ArticlePost.objects.all()

    if search:
        article_list = ArticlePost.objects.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        search=''

    if column is not None:
        print(column)
        article_list=ArticlePost.objects.filter(Q(column_id=columnid))

    if tag and tag != 'None':
        article_list=article_list.filter(tags__name__in=[tag])

    if order == 'total_views':
        article_list=article_list.order_by('-total_views')

    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {'articles': articles, 'order': order, 'search': search, 'columns': columns, 'column': column,'tag':tag,}

    return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    comments = Comment.objects.filter(article=id)   # from comment app to display comments in the bottom of the article

    md = markdown.Markdown(
    extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',

        'markdown.extensions.toc'
    ]
    )

    article.body = md.convert(article.body)
    article.total_views += 1
    article.save(update_fields=['total_views'])    # for the display method


    comment_form = CommentForm()
    context = {'article': article, 'toc':md.toc, 'comments': comments,'comment_form':comment_form,}

    return render(request, 'article/detail.html', context)


@login_required(login_url='userprofile/login/')       # only registered user can create article
def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(request.POST,request.FILES)
        if article_post_form.is_valid():

            new_article = article_post_form.save(commit=False)

            new_article.author = User.objects.get(id=request.user.id)
            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
            new_article.save()
            article_post_form.save_m2m()
            return redirect("article:article_list")
        else:
            return HttpResponse("Error:The content of form is wrong.Please fill out the form again")

    else:
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        context = {'article_post_form': article_post_form, 'columns': columns,}
        return render(request, 'article/create.html', context)


@login_required(login_url='userprofile/login/')  # only the author can delete and update
def article_safe_delete(request, id):
    articleget = ArticlePost.objects.get(id=id)    # get the current article
    user = articleget.author
    if request.user != user:
        return HttpResponse("You do not have the right to delete the article!")
    if request.method == 'POST':

        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("Only allow post request")


@login_required(login_url='userprofile/login/')
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    user = article.author
    if request.user != user:
        return HttpResponse("You do not have the right to delete the article!")
    if request.method == "POST":
        article_post_form = ArticlePostForm(request.POST, request.FILES)
        if article_post_form.is_valid():
            if request.POST['column'] != 'none':
                article.column = ArticleColumn.objects.get(id=request.POST['column'])
            else:
                article.column = None

            if request.FILES.get('picture'):
                article.picture = request.FILES.get('picture')

            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("Error:The content of form is wrong.Please fill out the form again")

    else:
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        context = {'article': article, 'article_post_form': article_post_form, 'columns': columns,}
        return render(request, 'article/update.html', context)
