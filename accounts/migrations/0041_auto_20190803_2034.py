# Generated by Django 2.1.7 on 2019-08-03 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20190802_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Class',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Section',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
