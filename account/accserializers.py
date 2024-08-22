from rest_framework.serializers import ModelSerializer
from main.models import *
from account.models import*
from main.serializers import *

class UserDoctorSerializer(ModelSerializer):
    workplace = HospitalSerializer()
    class Meta:
        model = UserDoctor
        fields = ['full_name', 'specialty', 'workplace', 'rating']


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['home_location', 'phone_number']

class UserSerializer(ModelSerializer):
    contact = UserInfoSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'sur_name', 'contact', 'birth_date', 'age',]


class HistorySerializer(ModelSerializer):
    hospital = HospitalSerializer(read_only=True)
    doctor = UserDoctorSerializer(read_only=True)
    diseases = DiseasesSerializer(many=True)
    medicines = MedicinesSerializer(many=True)
    antibiotic = AntibioticSerializer(read_only=True, many=True)

    class Meta:
        model = History
        fields = ['hospital', 'doctor', 'diseases', 'medicines', 'antibiotic']


class HealthProfileSerializer(ModelSerializer):
    class Meta:
        model = HealthProfile
        fields = ['blood_group_choices', 'blood_pressure_systolic', 'blood_pressure_diastolic']


class ChildInfoSerializer(ModelSerializer):
    class Meta:
        model = ChildInfo
        fields = ['home_location', 'phone_number']


class ChildSerialzier(ModelSerializer):
    contact = ChildInfoSerializer()
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'sur_name', 'contact', 'birth_date', 'age']


class ChildDiogenesSerializer(ModelSerializer):
    child = ChildSerialzier(read_only=True)
    hospital = HospitalSerializer(read_only=True)
    doctor = UserDoctorSerializer(read_only=True)
    diseases = DiseasesSerializer(many=True)
    medicines = MedicinesSerializer(many=True)
    antibiotic = AntibioticSerializer(read_only=True, many=True)

    class Meta:
        model = ChildDiogenes
        fields = ['child', 'hospital', 'doctor', 'diseases', 'medicines', 'antibiotic']


class FamilyUserInfoSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    hospital = HospitalSerializer(read_only=True)
    doctor = UserDoctorSerializer(read_only=True)
    diseases = DiseasesSerializer(many=True)
    medicines = MedicinesSerializer(many=True)
    antibiotic = AntibioticSerializer(read_only=True, many=True)

    class Meta:
        model = History
        fields = ['user', 'hospital', 'doctor', 'diseases', 'medicines', 'antibiotic']


class FamilySerializer(ModelSerializer):
    user = FamilyUserInfoSerializer(read_only=True, many=True)
    child = ChildDiogenesSerializer(read_only=True, many=True)

    class Meta:
        model = Family
        fields = ['user', 'child']