from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'universities', views.UniversityViewSet)

urlpatterns = [
    # path("universities/", views.UniversityAPIView.as_view(), name="universities_list.url"),
    # path("universities/<int:pk>/", views.UniversityDetailAPIView.as_view(), name="universities_detail.url"),
    path("", include(router.urls))

]