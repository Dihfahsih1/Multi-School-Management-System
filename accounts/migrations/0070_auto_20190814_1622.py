# Generated by Django 2.1.7 on 2019-08-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0069_auto_20190814_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='birth_date',
            field=models.CharField(max_length=100),
        ),
    ]
