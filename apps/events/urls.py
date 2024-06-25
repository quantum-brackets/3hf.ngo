from django.urls import path, include

from . import views


urlpatterns = [
   path('', views.EventsView.as_view(), name='events'),
   path('<slug:slug>/', views.EventsView.as_view(), name='events'),
   path('json/<slug:slug>/', views.event_detail_json, name='event-detail-json'),
   path('<int:event_id>/register/', views.register_for_event, name='event_registration'),
]
