# Generated by Django 3.2.3 on 2021-05-31 19:13

import core.models.patient
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_user_is_agreements'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.patient.photo_file_name),
        ),
    ]