# Generated by Django 2.1.7 on 2019-07-31 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_transport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School', models.CharField(max_length=130)),
                ('RouteTitle', models.CharField(max_length=130)),
                ('StartRoute', models.CharField(max_length=130)),
                ('EndRoute', models.CharField(max_length=130)),
                ('Notes', models.CharField(max_length=130)),
            ],
        ),
    ]
