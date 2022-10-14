# Generated by Django 4.1.1 on 2022-10-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userSystem', '0003_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_Type',
            field=models.CharField(choices=[('HOSADMIN', 'Hospital Admin'), ('DOCTOR', 'Doctor'), ('PATIENT', 'Patient')], default='NULL', max_length=10),
        ),
    ]