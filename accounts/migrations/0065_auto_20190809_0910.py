# Generated by Django 2.1.7 on 2019-08-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0064_auto_20190809_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersinformation',
            name='Responsibility',
            field=models.CharField(choices=[('Mathematics', 'Mathematics'), ('English', 'English'), ('History', 'History'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Economics', 'Economics')], max_length=100),
        ),
    ]
