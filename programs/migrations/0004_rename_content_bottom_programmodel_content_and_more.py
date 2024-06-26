# Generated by Django 5.0.1 on 2024-02-19 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_alter_programmodel_slug_programmodel_icon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programmodel',
            old_name='content_bottom',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='programmodel',
            name='content_up',
        ),
        migrations.AddField(
            model_name='programmodel',
            name='title_link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProgramDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.programmodel')),
            ],
        ),
    ]
