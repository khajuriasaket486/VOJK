# Generated by Django 2.2.4 on 2020-09-04 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
    ]
