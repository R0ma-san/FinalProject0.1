from .models import University
from .serializers import UniversitySerializer 
from django_filters.rest_framework import DjangoFilterBackend
from .service import UniversityFilter, GetOrIsAdmin
from rest_framework import viewsets

    
class UniversityViewSet(viewsets.ModelViewSet):

    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [GetOrIsAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UniversityFilter
    search_fields = ['name', 'body']
