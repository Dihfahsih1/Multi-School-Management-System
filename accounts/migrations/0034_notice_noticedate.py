# Generated by Django 2.1.7 on 2019-08-02 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='NoticeDate',
            field=models.CharField(default='02-July-2019', max_length=130),
        ),
    ]