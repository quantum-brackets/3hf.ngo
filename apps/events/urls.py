from django.urls import path, include

from . import views


urlpatterns = [
   path('upcoming/', views.UpcomingEventsView.as_view(), name='upcoming_events'),
   path('upcoming/<slug:slug>/', views.event_detail_json, name='event-detail-json'),
   path('concluded/', views.ConcludedEventsListView.as_view(), name='concluded_events'),
   path('concluded/<slug:slug>/', views.ConcludedEventsDetailsView.as_view(), name='concluded_event_details'),
   path('upcoming/<int:event_id>/register/', views.register_for_event, name='event_registration'),
]
