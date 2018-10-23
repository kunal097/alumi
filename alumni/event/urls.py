from django.urls import path
from .views import home,complete_profile,add_event

urlpatterns = [
    
    
path('profile/<ruser>',complete_profile,name='profile'),
path('event',add_event,name='event'),
path('',home),
    

]
