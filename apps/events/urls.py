from django.urls import path, include

from . import views


urlpatterns = [
   path('upcoming/', views.UpcomingEventsView.as_view(), name='upcoming_events'),
]
