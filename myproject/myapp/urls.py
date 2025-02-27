from django.contrib import admin
from django.urls import path, include  # include для включения маршрутов из другого модуля

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут административной панели Django
    path('api/', include('myapp.urls')),  # Включаем маршруты API из приложения myapp
]
from rest_framework import routers
from .views import MyViewSet  # Импортируем ViewSet из views.py

router = routers.DefaultRouter()
router.register(r'myview', MyViewSet, basename='myview')  # Регистрируем маршрут для ViewSet

urlpatterns = router.urls  # Присваиваем маршруты роутера к urlpatterns