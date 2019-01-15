from django.urls import path, re_path
from .views import index, room

app_name = 'chatapp'


urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room')
]
