# Generated by Django 2.1.7 on 2019-08-06 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_auto_20190806_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='SchooCode',
            new_name='SchoolCode',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='SchooName',
            new_name='SchoolName',
        ),
    ]
