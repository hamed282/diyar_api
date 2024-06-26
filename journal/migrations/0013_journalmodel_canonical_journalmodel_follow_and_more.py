# Generated by Django 5.0.3 on 2024-06-01 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0012_remove_tagmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalmodel',
            name='canonical',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journalmodel',
            name='follow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journalmodel',
            name='index',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journalmodel',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
