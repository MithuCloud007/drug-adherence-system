# Generated by Django 5.0 on 2023-12-31 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0005_remove_prescription_taken_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='drug_name',
            field=models.CharField(choices=[('isoniazid', 'Isoniazid'), ('rifampin ', 'Rifampin '), ('pyrazinamide ', 'Pyrazinamide'), ('ethambutol', 'Ethambutol '), ('streptomycin ', 'Streptomycin')], max_length=200),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='taken_time1',
            field=models.CharField(blank=True, choices=[('morning', 'Morning'), ('midday', 'Midday'), ('night', 'Night')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='taken_time2',
            field=models.CharField(blank=True, choices=[('morning', 'Morning'), ('midday', 'Midday'), ('night', 'Night')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='taken_time3',
            field=models.CharField(blank=True, choices=[('morning', 'Morning'), ('midday', 'Midday'), ('night', 'Night')], max_length=200, null=True),
        ),
    ]
