# Generated by Django 3.1.5 on 2023-07-23 17:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230723_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazimodel',
            name='icerik',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
