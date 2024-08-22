# Generated by Django 5.0.7 on 2024-08-06 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antibiotic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=55)),
                ('phone_number', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('type', models.CharField(choices=[('state_hospitial', 'State Hospitial'), ('private_hospitial', 'Private Hospitial')], default='state_hospital', max_length=55)),
                ('department', models.ManyToManyField(to='main.departament')),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.hospitalcontact')),
            ],
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('need_antibiotic', models.ManyToManyField(to='main.antibiotic')),
                ('need_medicine', models.ManyToManyField(to='main.medicines')),
            ],
        ),
    ]
