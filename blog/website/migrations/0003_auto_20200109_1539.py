# Generated by Django 3.0.2 on 2020-01-09 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_categorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categorie',
            new_name='category',
        ),
    ]
