# Generated by Django 5.0 on 2023-12-21 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyprogram',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10),
        ),
    ]