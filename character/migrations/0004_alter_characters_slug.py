# Generated by Django 4.1.7 on 2023-02-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0003_alter_characters_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='slug',
            field=models.SlugField(default=' ', null=True),
        ),
    ]