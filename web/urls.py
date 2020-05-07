from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('publications/', views.publications, name='publications'),
    path('user_<int:user_id>', views.user, name='user'),
    path('blog_<int:publication_id>', views.publication, name='publication'),
    path('blog_<int:publication_id>/add_comment/', views.add_comment, name='add_comment'),
    path('users/', views.users, name='users'),
    path('register/', views.register, name='register'),
    path('new_publication/', views.new_publication, name='new_publication'),

]
