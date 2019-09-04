# Generated by Django 2.1.7 on 2019-08-30 09:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20190828_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='feecollection',
            name='Section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Sectioninformation'),
        ),
        migrations.AlterField(
            model_name='studentpresence',
            name='Attendance_Date',
            field=models.DateField(default=datetime.datetime(2019, 8, 30, 9, 11, 29, 872460, tzinfo=utc)),
        ),
    ]