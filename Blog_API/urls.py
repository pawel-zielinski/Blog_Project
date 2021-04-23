from django.urls import path
from . import views


app_name = 'Blog_API'

urlpatterns = [
    path('', views.BlogList.as_view(), name = 'blog_list'),
    path('create_blog/', views.CreateBlog.as_view(), name = 'create_blog'),
    path('details/<slug:slug>', views.blog_details, name = 'blog_details'),
    path('like/<pk>/', views.like, name = 'liked_post'),
    path('dislike/<pk>/', views.dislike, name = 'disliked_post'),
    path('my-blogs/', views.MyBlog.as_view(), name = 'my_blogs'),
    path('edit-blog/<pk>/', views.UpdateBlog.as_view(), name = 'update_blog'),
]
