from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from main.models import *
from account.models import *
from main.serializers import *
from account.accserializers import *

@api_view(['POST'])
def sign_up(request):
    data = request.data
    first_name = data['first_name']
    last_name = data['last_name']
    sur_name = data['sur_name']
    username = data['username']
    password = data['password']
    home_location = data['home_location']
    phone_number = data['number']
    blood_group = data['blood_group']
    blood_pressure_systolic = data['blood_pressure_systolic']
    blood_pressure_diastolic = data['blood_pressure_diastolic']
    contact = UserInfo.objects.create(
        home_location=home_location,
        phone_number=phone_number
    )
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        contact=contact,
        sur_name=sur_name,
        username=username,
        password=password
    )
    health_profile = HealthProfile.objects.create(
        user=user,
        blood_group_choices=blood_group,
        blood_pressure_systolic=blood_pressure_systolic,
        blood_pressure_diastolic=blood_pressure_diastolic
    )
    token = Token.objects.get_or_create(user=user)
    context = {
        'message': 'Register Seccsusfully!',
        'token': token[0].key
    }
    return Response(context, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    data = request.data
    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user:
        token = Token.objects.get_or_create(user=user)
        context = {
            'message': 'SignIn Seccsusfully!',
            'token': token[0].key
        }
        return Response(context, status=status.HTTP_200_OK)
    else:
        return Response("User not exist!", status=status.HTTP_401_UNAUTHORIZED)
    
