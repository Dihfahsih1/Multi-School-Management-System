# Generated by Django 2.1.7 on 2019-08-14 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0070_auto_20190814_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdata',
            name='FatherPhoto',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='MotherPhoto',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='TransferCertificate',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='image',
        ),
    ]
