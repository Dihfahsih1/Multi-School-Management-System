# Generated by Django 2.1.7 on 2019-08-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_auto_20190809_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersinformation',
            name='JoiningDate',
            field=models.CharField(default='15-10-1990', max_length=130),
        ),
    ]
