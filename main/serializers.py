from rest_framework.serializers import ModelSerializer
from .models import Books


class BookSerializator(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'