from akins_api.filter import (DynamicDroneFilter, DynamicCameraFilter)
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

from .serlializers import (DroneSerializer, CameraSerializer)
from .models import *
from akins_api import serlializers
# Create your views here.


# Show a veri nice overview of how to use the api
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'All drones & search by fields': '/drone',
        'Add, Update & Dele': '/drone/pk',

        'All Camera & search by fields': '/camera',



        'JSON Web Token ': '/token',
        'JSON Web Token Refresh': '/token/refresh'
    }

    return Response(api_urls)


# List all drones into the DB and permit
class drone_view(generics.ListCreateAPIView):
    #search_fields = ['brand']
    filter_backends = (DynamicDroneFilter,)

    # https://www.django-rest-framework.org/api-guide/relations/
    # Refactoring: line bellow is better than queryset = Drone.objects.all()
    #  No additional database hits required
    queryset = Drone.objects.all().prefetch_related('supported_cameras')
    serializer_class = DroneSerializer


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


# Area for Camera Model

# List all cameras into the DB
class camera_view(generics.ListCreateAPIView):

    search_fields = ['model']
    filter_backends = (DynamicCameraFilter,)

    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    # TODO: Implemente in the future
    #permission_classes = [IsAdminUser]
