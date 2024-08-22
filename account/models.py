from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import *

class UserDoctor(models.Model):
    full_name = models.CharField(max_length=77)
    specialty = models.CharField(max_length=55)
    workplace = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.full_name


class History(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='history')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(UserDoctor, on_delete=models.CASCADE)
    diseases = models.ManyToManyField(Diseases)
    medicines = models.ManyToManyField(Medicines)
    antibiotic = models.ManyToManyField(Antibiotic)

    def __str__(self) -> str:
        return f"{self.user.first_name} - {self.user.last_name} - {self.user.sur_name}"

class UserInfo(models.Model):
    home_location = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=13, unique=True)

    
    def __str__(self) -> str:
        return f"{self.pk}"
    

class HealthProfile(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    blood_group_choices = models.CharField(max_length=55, default='a+', choices=((
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O-'),
        ('o-', 'O-')
    )))
    blood_pressure_systolic = models.IntegerField()
    blood_pressure_diastolic = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.blood_group_choices}"


class User(AbstractUser):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    sur_name = models.CharField(max_length=55)
    contact = models.ForeignKey(UserInfo, on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.first_name} - {self.first_name}"
    
class ChildInfo(models.Model):
    home_location = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=17, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.home_location
    
class Child(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    sur_name = models.CharField(max_length=55)
    contact = models.ForeignKey(ChildInfo, on_delete=models.CASCADE)
    birth_date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.first_name

class ChildDiogenes(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(UserDoctor, on_delete=models.CASCADE)
    diseases = models.ManyToManyField(Diseases)
    medicines = models.ManyToManyField(Medicines)
    antibiotic = models.ManyToManyField(Antibiotic)

    def __str__(self) -> str:
        return f"{self.child.first_name} - {(str(self.diseases.name))}"
    

class ChildHealthProfile(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    blood_group_choices = models.CharField(max_length=55, default='a+', choices=((
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O-'),
        ('o-', 'O-')
    )))

    def __str__(self) -> str:
        return f"{self.child.first_name}"
    

class Family(models.Model):
    name = models.CharField(max_length=55)
    user = models.ManyToManyField(History, related_name='families')
    child = models.ManyToManyField(ChildDiogenes, related_name='families')

    def __str__(self) -> str:
        return self.name