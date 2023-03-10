# Generated by Django 4.1.7 on 2023-03-09 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0007_periode_season'),
        ('character', '0010_characters_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='periode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helper.periode'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helper.season'),
        ),
    ]
