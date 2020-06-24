from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('post_comment/<int:article_id>/',views.post_comment,name='post_comment'),
    path('post_comment/<int:article_id>/<int:parent_comment_id>',views.post_comment,name='comment_reply'),
    path('delete_comment/<int:id>/',views.delete_comment,name='delete_comment'),
]