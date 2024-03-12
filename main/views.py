
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Books
from .serializers import BookSerializator


@api_view(['GET'])
def get_books(request):
    cat = Books.objects.all()
    serializer = BookSerializator(cat,many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT'])
def put_books(request):
    try:
        cat = Books.objects.get(id=pk)
        serializer = BookSerializator(instance=cat, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    except Books.DoesNotExist:
        return Response('not found')
    
    
@api_view(['DELETE'])
def delete_books(request, pk):
    try:
        cat = Books.objects.get(id=pk)
        cat.delete()
        return Response('successfully delete', status=200)
    except Books.DoesNotExist:
        return Response('not found')
    
    
@api_view(['GET'])
def get_books_by_id(request, pk):
    try:
        cat = Books.objects.get(id=pk)
        serializer = BookSerializator(cat)
        return Response(serializer.data, status=200)
    except Books.DoesNotExist:
        return Response('Not found')
    

    
@api_view(['POST'])
def post_books(request):
    serializer = BookSerializator(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=200)
    
