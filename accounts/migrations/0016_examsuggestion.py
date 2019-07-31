# Generated by Django 2.1.7 on 2019-07-31 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20190731_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School', models.CharField(max_length=130)),
                ('SuggestionTitle', models.CharField(max_length=130)),
                ('Suggestion', models.FileField(max_length=130, upload_to='')),
                ('Notes', models.TextField(blank=True, max_length=150)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Classinformation')),
                ('Exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ExamTerm')),
                ('Subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Subjects')),
            ],
        ),
    ]
