# Generated by Django 3.1.6 on 2021-02-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='link',
            field=models.CharField(max_length=400),
        ),
    ]
