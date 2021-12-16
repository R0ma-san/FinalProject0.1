from django.db.models.fields import CharField
from django_filters import rest_framework as filters
from .models import University
from rest_framework import permissions

class CharFieldInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class UniversityFilter(filters.FilterSet):
    category = CharFieldInFilter(field_name = 'category__name', lookup_expr='in')
    specialization = CharFieldInFilter(field_name = 'specialization__name', lookup_expr='in')
    price = filters.RangeFilter()
    TOEFL = filters.RangeFilter()
    SAT = filters.RangeFilter()
    GPA = filters.RangeFilter()
    IELTS = filters.RangeFilter()

    class Meta:
        model = University
        fields = ['category', 'specialization', 'price', 'TOEFL', 'SAT', "GPA", "IELTS"]


class GetOrIsAdmin(permissions.BasePermission):        

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.is_staff and request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            return True
        
        if request.method == 'GET':
            return True

        return False