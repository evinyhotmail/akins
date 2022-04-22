from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)


from akins_api.models import *
from akins_api.filter import (DynamicDroneFilter, DynamicCameraFilter)
from .serializers import (DroneSerializer, CameraSerializer)

# Create your views here.


# Show a veri nice overview of how to use the api
@api_view(['GET'])
def ApiOverview(request):

    context_url = {
        'all_items': '/drones',
        'Search by id': '/?id=drone_id',
        'Search by name': '/?name=drone_name',
        'Search by brand': '/?brand=drone_brand',
        'Search by serial number': '/?serial_number=drone_serial_number',
        'Search by Camera model': '/?cameras__weight=weight',

        'Add a drone': '/create',
        'Update a drone': '/update/pk',
        'Delete a drone': '/item/pk/delete'
    }

    return Response(context_url)


class drone_list(generics.ListAPIView):

    # queryset = Drone.objects.all()
    # Oficial doc: rhttps://www.django-rest-framework.org/api-guide/relations/
    # Better, No additional database hits required
    queryset = Drone.objects.prefetch_related('cameras')
    serializer_class = DroneSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = get_modelfieldlist(Drone, Camera)
    # filterset_fields = ['id', 'name', 'brand', 'cameras__weight']


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


# Used to update or delete a drone into the DB
@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def drone_crud(request, pk, format=None):
    """
    Retrieve, update or delete a drone
    """
    # Defining standard context error message
    context = {
        'detail': 'UNAUTHORIZED USER',

    }

    try:
        drone = Drone.objects.get(pk=pk)
    except Drone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
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
# class camera_view(generics.ListAPIView):

#     queryset = Camera.objects.all()
#     serializer_class = CameraSerializer

#     filter_backends = (DjangoFilterBackend)

#     filterset_fields = ['model', 'brand', 'weight', 'megapixel']

#     # TODO: Implemente in the future
#     #permission_classes = [IsAdminUser]


class camera_view(generics.ListAPIView):

    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'model', 'brand', 'weight', 'megapixel']
