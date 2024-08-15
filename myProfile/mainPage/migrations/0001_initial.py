# Generated by Django 5.0.4 on 2024-08-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Compute', 'Compute Services'), ('Database', 'Database Services'), ('Networking', 'Networking Services'), ('DevOps', 'Development and DevOps'), ('Migration', 'Migration Services'), ('Managed', 'Managed Services'), ('Support', 'Support and Consulting')], max_length=50)),
            ],
        ),
    ]