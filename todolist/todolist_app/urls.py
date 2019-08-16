from django.urls import path
from .views import (
    Home,
    About,
    Delete,
    Cross,
    Uncross
)


app_name = 'todo'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('delete/<int:list_id>',Delete.as_view(), name='delete'),
    path('cross/<int:list_id>',Cross.as_view(), name='cross'),
    path('uncross/<int:list_id>',Uncross.as_view(), name='uncross'),
]
