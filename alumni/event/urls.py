from django.urls import path
from .views import home,complete_profile,add_event,get_event,profile

urlpatterns = [
    
    
path('profile/<ruser>',complete_profile,name='profile'),
path('event-list',get_event,name='get_event'),
path('event',add_event,name='event'),
path('profile',profile,name='profile'),
path('',home),
    

]
