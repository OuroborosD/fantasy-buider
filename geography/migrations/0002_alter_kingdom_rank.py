# Generated by Django 4.1.7 on 2023-03-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kingdom',
            name='rank',
            field=models.SmallIntegerField(choices=[(1, 'Kingdom'), (2, 'empire'), (3, 'republic')]),
        ),
    ]
