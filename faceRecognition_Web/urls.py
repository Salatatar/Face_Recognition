from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('add-Image/', include('add_image.urls')),
    path('report-Data/', include('report_data.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
