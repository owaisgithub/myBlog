from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('blog/<int:blog_id>/', views.readBlog, name='blog'),
    path('blog/<int:blog_id>/comment/', views.comment, name='comment'),
    path('writeBlog/', views.writeBlog, name='writeBlog'),
    path('blog/postEntry/', views.postEntry, name='postEntry'),
    path('blog/<int:blog_id>/comment/add/', views.addComment, name='addComment'),
    path('blog/<int:blog_id>/postComment/', views.postComment, name='postComment'),
]
