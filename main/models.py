from django.db import models


class HospitalContact(models.Model):
    location = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.phone_number
    
class Departament(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=55)
    type = models.CharField(max_length=55, default='state_hospital', choices=((
        ('state_hospitial', 'State Hospitial'),
        ('private_hospitial', 'Private Hospitial')
    )))
    contact = models.OneToOneField(HospitalContact, on_delete=models.CASCADE)
    department = models.ManyToManyField(Departament)

class Antibiotic(models.Model):
    name = models.CharField(max_length=55)
    
    def __str__(self) -> str:
        return self.name
        
class Medicines(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    
class Diseases(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    need_medicine = models.ManyToManyField(Medicines)
    need_antibiotic = models.ManyToManyField(Antibiotic)

    def __str__(self) -> str:
        return self.name