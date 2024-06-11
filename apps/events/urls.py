from django.urls import path, include

from . import views


urlpatterns = [
   path('', views.UpcomingEventsView.as_view(), name='events'),
   path('json/<slug:slug>/', views.event_detail_json, name='event-detail-json'),
   path('', views.ConcludedEventsListView.as_view(), name='concluded_events'),
   path('<slug:slug>/', views.ConcludedEventsDetailsView.as_view(), name='concluded_event_details'),
   path('upcoming/<int:event_id>/register/', views.register_for_event, name='event_registration'),
]
