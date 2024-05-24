from django.urls import path, include

from . import views


urlpatterns = [
   path('upcoming/', views.UpcomingEventsView.as_view(), name='upcoming_events'),
   path('upcoming/<int:pk>/', views.event_detail_json, name='event-detail-json'),
   path('concluded/', views.ConcludedEventsView.as_view(), name='concluded_events'),
   path('concluded/<int:pk>/', views.ConcludedEventsDetailsView.as_view(), name='concluded_event_details'),
]
