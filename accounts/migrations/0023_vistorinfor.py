# Generated by Django 2.1.7 on 2019-08-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20190801_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='VistorInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School', models.CharField(max_length=130)),
                ('Name', models.CharField(max_length=130)),
                ('Phone', models.CharField(max_length=130)),
                ('ComingFrom', models.CharField(max_length=130)),
                ('ToMeetUserType', models.CharField(max_length=130)),
                ('ReasonToMeet', models.CharField(max_length=130)),
                ('Notes', models.TextField(max_length=110)),
            ],
        ),
    ]