# Generated by Django 3.0.2 on 2020-01-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200109_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
