# Generated by Django 3.2 on 2021-11-12 01:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_chore_starttask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
    ]
