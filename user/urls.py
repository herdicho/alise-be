from django.conf.urls import url
from django.urls import path
from .views import UserRegister

urlpatterns = [
    #url(r'content/$', ContentList.as_view(), name='content_list'),
    #url(r'content/<int:pk>/$', ContentDetail.as_view(), name='content_detail'),
    path('register/', UserRegister.as_view()),

]