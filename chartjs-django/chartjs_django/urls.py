from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chartjs_drf_ajax/', include('chartjs_drf_ajax.urls')),
]
