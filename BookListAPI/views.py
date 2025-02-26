from django.shortcuts import render
from rest_framework import status, generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttles import TenCallsPerMinute
from rest_framework.permissions import IsAdminUser

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


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"Some secret message"})

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"Only managers should see this"})
    else:
        return Response({"message":"You cant see this"},403)

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"Successful"})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response({"message":"message for the logged in user only"})


@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth_ten(request):
    return Response({"message":"message for the logged in user only ten per minute"})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def managers(request):
    return Response({"message":"ok"})