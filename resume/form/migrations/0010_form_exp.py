# Generated by Django 4.2.2 on 2023-08-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_form_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='exp',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
