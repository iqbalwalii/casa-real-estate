# Generated by Django 3.0.8 on 2020-07-12 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='is_pulished',
            new_name='is_published',
        ),
    ]
