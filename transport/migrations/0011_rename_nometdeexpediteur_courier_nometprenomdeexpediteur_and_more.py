# Generated by Django 4.1.2 on 2023-04-06 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0010_courier_reserve_nometprenom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courier',
            old_name='nomEtDeExpediteur',
            new_name='nomEtPrenomDeExpediteur',
        ),
        migrations.RenameField(
            model_name='courier',
            old_name='nomDuDestinatair',
            new_name='nomEtPrenomDuDestinatair',
        ),
    ]
