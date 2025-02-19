from django.shortcuts import render
from rest_framework import status, generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET', 'POST'])
def books(request):
    return Response('List of the books', status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if author:
            return Response(f'List of the books by {author}', status=status.HTTP_200_OK)

        return Response('List of the books', status=status.HTTP_200_OK)

    def post(self, request):
        # return Response('Create a new book', status=status.HTTP_201_CREATED)
        return Response({"Titless":request.data.get('title')}, status=status.HTTP_201_CREATED)

class Book(APIView):
    def get(self, request, pk):
        return Response({"Message":"single book with id "+str(pk)}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status=status.HTTP_200_OK)

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer