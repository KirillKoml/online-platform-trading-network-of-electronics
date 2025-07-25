from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Урлы приложения shops
    path('', include('shops.urls', namespace='shops')),

    # Урлы приложения staff
    path('staff/', include('staff.urls', namespace='staff')),
]
