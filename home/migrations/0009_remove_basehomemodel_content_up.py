# Generated by Django 5.0.1 on 2024-02-16 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_basehomemodel_content_up'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basehomemodel',
            name='content_up',
        ),
    ]
