# Generated by Django 3.2 on 2021-11-12 01:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_chore_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chore',
            name='description',
        ),
        migrations.AddField(
            model_name='chore',
            name='startTask',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chore',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='chore',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Active/Inactive'),
        ),
    ]
