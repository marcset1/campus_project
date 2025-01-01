from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from annonce import views

router = DefaultRouter()
router.register(r'locations', views.LocationViewSet)
router.register(r'characteristics', views.CharacteristicViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]







