from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name='home'),
    path('new/',blog.views.new, name='new'),
    path('post/<int:pk>',blog.views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit',blog.views.post_edit,name='post_edit'),
    path('post/<int:pk>/remove',blog.views.post_remove, name='post_remove'),
]
