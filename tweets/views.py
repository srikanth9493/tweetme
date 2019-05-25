
from django.shortcuts import render
from .models import Tweet
# Create your views here.
from .models import Tweet
from django.views.generic import ListView,DetailView
from django.shortcuts import  get_object_or_404
from .form import  TweetForm


class TweetListView(ListView):
    template_name = "tweets/list_view.html";
    model = Tweet
    def get_context_data(self,**kwargs):
        context=super().get_context_data()
        context["tweet_list"]=Tweet.objects.all();
        return context

class TweetDetailView(DetailView):

    template_name = "tweets/detail_view.html"
    model = Tweet
    queryset = Tweet.objects.all();
    context_object_name = "tweet_obj"


    def get_object(self):
        id_=self.kwargs.get("id");
        print(id_)
        return get_object_or_404(Tweet, id=id_)

from django.views.generic import  CreateView

class TweetCreateView(CreateView):

    form_class = TweetForm
    template_name = "tweets/create_view.html"
    success_url = "tweets/create_view.html"

    def form_valid(self, form):
        form.instance.user=self.request.user;
        return  super().form_valid(form)






def tweet_list_view(request):
    context=dict()
    context["tweet_list"]=Tweet.objects.all();

    return  render(request,"tweets/list_view.html",context)

def tweet_detail_view(request,id):
    context={}
    context["tweet_obj"]=Tweet.objects.get(id=id);
    return  render(request,"tweets/detail_view.html",context)

def tweet_delete_view(request):

    return  render(request,"tweets/delete_view.html",{})

def tweet_update_view(request):
    return  render(request,"tweets/update_view.html",{})




