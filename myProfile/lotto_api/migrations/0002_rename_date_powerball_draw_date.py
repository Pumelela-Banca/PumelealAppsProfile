# Generated by Django 5.0.4 on 2024-09-05 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotto_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='powerball',
            old_name='date',
            new_name='draw_date',
        ),
    ]
