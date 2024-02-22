from django.urls import path
from . import views

# url patterns are basically the url in the http request -> address bar
urlpatterns = [
    # name is the route - in this case  ' ' - name 
    #  path takes kwargs like name and args
    path('', views.home, name='home')
]