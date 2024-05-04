from django.urls import path, include

from . import views


urlpatterns = [
   path('upcoming/', views.UpcomingEventsView.as_view(), name='upcoming_events'),
   path('upcoming/<int:pk>/', views.event_detail_json, name='event-detail-json'),
]
