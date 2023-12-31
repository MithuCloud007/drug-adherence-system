# Generated by Django 5.0 on 2023-12-31 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0002_doctor_remove_patient_doctor_contact_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='prescription_date',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='dose',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='dose_time',
        ),
        migrations.AddField(
            model_name='prescription',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='taken_time',
            field=models.CharField(choices=[('morning', 'Morning'), ('midday', 'Midday'), ('night', 'Night')], default='morning', max_length=50),
        ),
    ]
