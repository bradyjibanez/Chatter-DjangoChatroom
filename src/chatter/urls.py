from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from chat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace='chat')),
]