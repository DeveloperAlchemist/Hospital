from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, BasePermission
from main.models import *
from account.models import *
from main.serializers import *
from account.accserializers import *


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        doctor = UserDoctor.objects.filter(user=user)
        if doctor:
            return True
        else:
            return False

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_information(request):
    user = request.user
    history = History.objects.filter(user=user)
    history_serializer = HistorySerializer(instance=history, many=True).data
    health_profile = HealthProfile.objects.filter(user=user)
    health_profile_serializer = HealthProfileSerializer(instance=health_profile, many=True).data
    families = Family.objects.filter(user__user=user).distinct()
    family_serializer = FamilySerializer(instance=families, many=True).data
    context = {
        'health_profile': health_profile_serializer,
        'history': history_serializer,
        'family': family_serializer,
    }
    return Response(context, status=status.HTTP_200_OK)



# @api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsDoctor, IsAuthenticated])
# def doctor_menegment(request):