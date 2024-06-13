from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('heartsandhands.urls')),
    path('events/', include("events.urls")),
    path('summernote/', include('django_summernote.urls'))
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = '3hf Admin'
admin.site.site_header = 'Hearts and Hands Humanitarian Foundation'