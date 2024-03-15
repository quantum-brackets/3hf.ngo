from django.urls import path, include

from . import views


urlpatterns = [
   path('', views.HomeView.as_view(), name='home'),
   path('contact', views.ContactUsView.as_view(), name='contact_us'),
]
