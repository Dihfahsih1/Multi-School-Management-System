# Generated by Django 2.1.7 on 2019-08-08 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0060_auto_20190808_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectioninformation',
            name='StreamTeacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.TeachersInformation'),
        ),
    ]
