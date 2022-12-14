# Generated by Django 4.1.1 on 2022-10-19 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_alter_hospital_createdby'),
        ('doctor', '0003_remove_doctor_hospitalid'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.IntegerField(default=1)),
                ('doctorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('hospitalID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
        ),
    ]
