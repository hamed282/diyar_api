# Generated by Django 5.0.3 on 2024-06-06 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0016_alter_addtagmodel_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journalmodel',
            options={'verbose_name': 'Journal', 'verbose_name_plural': 'Journals'},
        ),
        migrations.AlterModelOptions(
            name='tagmodel',
            options={'verbose_name': 'Journal Tag', 'verbose_name_plural': 'Journal Tags'},
        ),
    ]
