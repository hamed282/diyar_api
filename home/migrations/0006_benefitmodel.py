# Generated by Django 5.0.1 on 2024-02-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_basehomemodel_user_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenefitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.TextField(default='trest')),
            ],
        ),
    ]
