# Generated by Django 4.1.7 on 2023-02-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_summary_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default=None),
        ),
    ]
