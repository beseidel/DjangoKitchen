
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.auth.models import User


# Create your models here.

#This is used for the queryset in class post

# This is a simple model


# This is a queryset model

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# need to add an import of a reverse
from django.urls import reverse


class Kitchen(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self,multiply=int(4)):
        return self.title

    # def __str__(self,<times>):
    #     return self.('multiply'=<int(times))>

    # need to get an absolute url...not sure why???
    def get_absolute_url(self):
        return reverse('kitchen-detail', kwargs={'pk': self.pk})

