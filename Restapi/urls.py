from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from appw import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

router.register('appw', views.StudentViewSet, basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
