# Generated by Django 4.2.2 on 2023-06-29 04:27

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_alter_form_cv_alter_form_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='cv',
            field=models.FileField(default=None, max_length=250, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/cv'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='form',
            name='file',
            field=models.FileField(default=None, max_length=250, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/cv'), upload_to=''),
        ),
    ]
