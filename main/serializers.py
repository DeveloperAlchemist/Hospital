from rest_framework.serializers import ModelSerializer
from main.models import *

class HospitalContactSerializer(ModelSerializer):
    class Meta:
        model = HospitalContact
        fields = ['location', 'phone_number', 'email']

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Departament
        fields = ['name']

class HospitalSerializer(ModelSerializer):
    department = DepartmentSerializer(many=True)
    contact = HospitalContactSerializer()

    class Meta:
        model = Hospital
        fields = ['name', 'type', 'contact', 'department']

class AntibioticSerializer(ModelSerializer):
    class Meta:
        model = Antibiotic
        fields = ['name']

class MedicinesSerializer(ModelSerializer):
    class Meta:
        model = Medicines
        fields = ['name', 'description']

class DiseasesSerializer(ModelSerializer):
    need_antibiotic = AntibioticSerializer(many=True)
    need_medicine = MedicinesSerializer(many=True)

    class Meta:
        model = Diseases
        fields = ['name', 'description', 'need_antibiotic', 'need_medicine']
        depth = 2

# << Main page, Serializer the end >> #