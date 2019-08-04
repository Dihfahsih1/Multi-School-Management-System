# Generated by Django 2.1.7 on 2019-08-02 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Subject',
        ),
        migrations.AddField(
            model_name='student',
            name='Section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Sectioninformation'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Guardian',
            field=models.CharField(max_length=130),
        ),
        migrations.AlterField(
            model_name='student',
            name='RelationshipWithGuardian',
            field=models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Uncle', 'Uncle'), ('Auntie', 'Auntie'), ('Other', 'Others')], max_length=130),
        ),
    ]