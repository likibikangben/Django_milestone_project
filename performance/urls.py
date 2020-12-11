from django.urls import path
from . import views 

urlpatterns = [
    path('', views.line_up, name='line_up'),
]
