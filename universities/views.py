from rest_framework import permissions, mixins, generics
import rest_framework
from .models import University
from .serializers import UniversitySerializer #, UniversityDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .service import UniversityFilter, GetOrIsAdmin
from rest_framework import viewsets

    
class UniversityViewSet(viewsets.ModelViewSet):

    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [GetOrIsAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UniversityFilter
    
# class UniversityAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

#     queryset = University.objects.all()
#     serializer_class = UniversitySerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = UniversityFilter
#     permission_classes = [permissions.IsAuthenticated,]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class UniversityDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):


#     queryset = University.objects.all()
#     serializer_class = UniversityDetailSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
