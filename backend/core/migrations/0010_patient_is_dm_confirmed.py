# Generated by Django 3.2.3 on 2021-05-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_dm_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]