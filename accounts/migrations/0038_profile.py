# Generated by Django 2.1.7 on 2019-08-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20190802_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=130)),
                ('Phone', models.CharField(max_length=130)),
                ('PresentAdress', models.CharField(max_length=130)),
                ('PermanentAddress', models.CharField(max_length=130)),
                ('Gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=130)),
                ('DateOfBirth', models.CharField(max_length=130)),
                ('Religion', models.CharField(max_length=130)),
                ('Email', models.CharField(max_length=130)),
                ('Photo', models.FileField(max_length=130, upload_to='')),
                ('Resume', models.FileField(max_length=130, upload_to='')),
                ('OtherInfo', models.TextField(max_length=120)),
            ],
        ),
    ]