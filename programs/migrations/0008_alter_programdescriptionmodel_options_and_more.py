# Generated by Django 5.0.1 on 2024-03-15 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0007_alter_programmodel_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programdescriptionmodel',
            options={'verbose_name': 'Program', 'verbose_name_plural': 'Program'},
        ),
        migrations.AlterField(
            model_name='programmodel',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Header'),
        ),
        migrations.AlterField(
            model_name='programmodel',
            name='title_link',
            field=models.CharField(max_length=100, verbose_name='Icon Title'),
        ),
    ]