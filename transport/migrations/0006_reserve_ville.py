# Generated by Django 4.1.7 on 2023-03-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0005_place_disponibilite_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('villeDepart', models.CharField(max_length=50)),
                ('villeArrive', models.CharField(max_length=50)),
                ('nombreDePlace', models.IntegerField()),
                ('typeVoyage', models.CharField(max_length=50)),
                ('dateReservation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
    ]