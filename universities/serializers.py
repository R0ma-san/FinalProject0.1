from rest_framework import serializers
from .models import Country, University

class UniversitySerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    specialization = serializers.SlugRelatedField(slug_field='name', read_only=True, many = True) 
    country = serializers.SlugRelatedField(slug_field='name', read_only=True)
    
    class Meta:

        model = University
        fields = ['id', 'name', 'country', 'body', 'images', 'url' ,'category', 'specialization', 'deadline_ed', 'deadline_rd', 'GPA', 'SAT', 'IELTS', 'TOEFL', 'price']
