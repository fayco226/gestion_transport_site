# Generated by Django 4.1.7 on 2023-02-22 18:10

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('nombre_de_places', models.IntegerField()),
                ('capacite_bagage', models.IntegerField()),
                ('nombre_de_car', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.TextField(max_length=100)),
                ('addresse', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('cnib', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Voyages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville_depart', models.CharField(max_length=200)),
                ('ville_arrive', models.CharField(max_length=200)),
                ('heure_depart', models.TimeField()),
                ('place_number', models.IntegerField()),
                ('prix', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.car')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage_programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville_depart', models.CharField(max_length=200)),
                ('ville_arrive', models.CharField(max_length=200)),
                ('heure_depart', models.TimeField()),
                ('prix', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.car')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.client')),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.voyages')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('nombre_de_place', models.IntegerField(default=100)),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.voyages')),
            ],
        ),
    ]