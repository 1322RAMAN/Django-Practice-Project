from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'This is a protected view.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secured_view(request):
    return Response({'message': 'Only authenticated users can see this.'})
