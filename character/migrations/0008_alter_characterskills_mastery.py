# Generated by Django 4.1.7 on 2023-03-08 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0007_skills_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterskills',
            name='mastery',
            field=models.SmallIntegerField(choices=[(1, 'beggining'), (2, 'intermediary'), (4, 'great completion'), (3, 'small completion'), (5, 'master')]),
        ),
    ]