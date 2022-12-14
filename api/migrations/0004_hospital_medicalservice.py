# Generated by Django 4.1.2 on 2022-10-14 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_country_delete_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=1000)),
                ('country_name', models.CharField(max_length=10000)),
                ('address', models.TextField()),
                ('website_url', models.CharField(max_length=10000)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_service', models.CharField(max_length=10000)),
                ('price', models.IntegerField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hospital')),
            ],
        ),
    ]
