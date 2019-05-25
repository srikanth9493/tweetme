"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from .views import  tweet_delete_view,tweet_detail_view,tweet_list_view,tweet_update_view,TweetListView,TweetDetailView,TweetCreateView
from  django.conf.urls import  url

urlpatterns = [
     url("^$",TweetListView.as_view()),
     url("delete_view",tweet_delete_view),
     url("update_view",tweet_update_view),
     url('(?P<id>[0-9]{1})/',TweetDetailView.as_view()),
     url("create_view/",TweetCreateView.as_view())

]


