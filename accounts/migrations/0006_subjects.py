# Generated by Django 2.1.7 on 2019-07-29 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subjectname', models.CharField(max_length=130)),
                ('Subjectcode', models.CharField(max_length=130)),
                ('Author', models.CharField(max_length=130)),
                ('Type', models.CharField(choices=[('Compulsory', 'Compulsory'), ('Options', 'Options')], max_length=130)),
                ('OtherNotes', models.TextField(blank=True, max_length=200)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Classinformation')),
                ('SubjectTeacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Teacher')),
            ],
        ),
    ]
