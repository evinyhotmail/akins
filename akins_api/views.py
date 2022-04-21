from akins_api.filter import DynamicSearchFilter
from rest_framework import filters, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)
from rest_framework.response import Response

from .serlializers import (DroneSerializer)
from .models import *
# Create your views here.


# FIXME: add all api url in order to provide a good lecture for the user
# Show a veri nice overview of how to use the api
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all drone items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


# List all drones into the DB
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def drone_list(request,  format=None):
    if request.method == 'GET':
        snippets = Drone.objects.all()
        serializer = DroneSerializer(snippets, many=True)
        return Response(serializer.data)


# Create a new one drone
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def drone_add(request,  format=None):
    if request.method == 'POST':
        serializer = DroneSerializer(data=request.data)
        # this will check if the json is valid and the user is part of support team
        if serializer.is_valid() and request.user.profile.is_user_support:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif not request.user.profile.is_user_support:
            context = {
                'error': '401',
                'message': 'UNAUTHORIZED USER',
            }
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Used to get, update or delete a drone into the DB
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def drone_detail(request, pk, format=None):
    """
    Retrieve, update or delete a drone
    """
    # Defining standard context error message
    context = {
        'error': '401',
        'message': 'UNAUTHORIZED USER',
    }

    try:
        drone = Drone.objects.get(pk=pk)
    except Drone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DroneSerializer(drone)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DroneSerializer(drone, data=request.data)
        if serializer.is_valid() and request.user.profile.is_user_support:
            serializer.save()
            return Response(serializer.data)
        elif not request.user.profile.is_user_support:
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if request.user.profile.is_user_support:
            drone.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)


class search_view(generics.ListCreateAPIView):
    search_fields = ['brand']
    filter_backends = (DynamicSearchFilter,)
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
