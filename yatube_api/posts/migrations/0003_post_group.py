# Generated by Django 3.2.16 on 2023-01-18 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230118_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.group'),
        ),
    ]
