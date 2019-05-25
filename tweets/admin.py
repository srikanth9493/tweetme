from django.contrib import admin
from .models import  Tweet
from .form import TweetForm
# Register your models here.
# admin.site.register(Tweet)

class TweetModelForm(admin.ModelAdmin):
     form = TweetForm

admin.site.register(Tweet,TweetModelForm)

