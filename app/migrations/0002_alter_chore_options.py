# Generated by Django 3.2 on 2021-10-22 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chore',
            options={'verbose_name': 'chore', 'verbose_name_plural': 'chores'},
        ),
    ]
