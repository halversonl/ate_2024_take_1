# Generated by Django 5.0.3 on 2024-05-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_input', '0003_alter_activity_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
