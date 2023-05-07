from django.urls import path
from . import views
from Buddy import settings
from django.conf.urls import include


urlpatterns = [
    
    path('submitblog', views.BlogCreateView.as_view(),name='createblog'),
    path('course', views.test3 , name='test3'),
    path('create',  views.CourseCreateView.as_view(),name='createcourse'),
    path('request', views.RequestCourseView.as_view(), name='requestcourse'),
    path('blog', views.test2.as_view(), name='test2'),
    path('quiz', views.test1.as_view(), name='test1'),
    path('', views.com, name='community'),



    ]