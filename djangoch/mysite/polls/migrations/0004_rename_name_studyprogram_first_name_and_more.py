# Generated by Django 5.0 on 2023-12-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_studyprogram_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studyprogram',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='studyprogram',
            name='last_name',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
