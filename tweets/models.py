from django.db import models
from  django.conf import settings
from django.core.exceptions import ValidationError
# Create your models here.

def validate_content(value):
    if(value=="abc"):
        raise   ValidationError("Value can not be ABC")
    return  value



class Tweet(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    content=models.CharField(max_length=140,validators=[validate_content])
    timestamp=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.user)


    # one of validation error. This method call before saving anything into the database
    # def clean(self):
    #     content=self.content
    #     if(content=="abc"):
    #         raise ValidationError("cannotb abc")
    #     return  super().clean()

