from django.contrib import admin
from django.urls import path,include
from dashboard import views
from django.contrib.auth import views as auth_view

app_name="dashboard"

urlpatterns = [
    path('',views.default,name='home'),
    path('logout/',views.logoutPage,name='logout'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.register,name='register'),
    path('post/',views.post,name='post'),
    path('update/',views.update,name='update'),
    path('profile/<int:pk>',views.profile_info,name='info'),
    path('follow/',views.follow_count,name='follow'),
    path('like_post/',views.like_post,name='like'),
    path('comment/',views.comment_input,name='comment'),
    path('show_comment/',views.show_comment,name='comment'),
    path('rest_api/list',views.account_list.as_view(),name='api-list'),
    path('rest_api/retrive/<int:pk>',views.account_retrive.as_view(),name='api-retrive'),


]