# Generated by Django 2.1.7 on 2019-08-08 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_auto_20190807_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Classinformation'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Sectioninformation'),
        ),
    ]