from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'universities', views.UniversityViewSet)

urlpatterns = [
     path("", include(router.urls))

]