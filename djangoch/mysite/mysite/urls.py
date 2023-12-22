
from django.contrib import admin
from django.urls import path,include
from polls.views import heybro,hi,home


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('polls.urls')),
    path("polls/",home),
    path("heybro/",heybro),
    path("hi/",hi),
]
