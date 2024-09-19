# Generated by Django 5.0.4 on 2024-09-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.CharField(max_length=50)),
                ('number_1', models.IntegerField()),
                ('number_2', models.IntegerField()),
                ('number_3', models.IntegerField()),
                ('number_4', models.IntegerField()),
                ('number_5', models.IntegerField()),
                ('div_winners_1', models.IntegerField()),
                ('div_winners_2', models.IntegerField()),
                ('div_winners_3', models.IntegerField()),
                ('div_winners_4', models.IntegerField()),
                ('div_prise_1', models.FloatField()),
                ('div_prise_2', models.FloatField()),
                ('div_prise_3', models.FloatField()),
                ('div_prise_4', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LottoP1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.CharField(max_length=50)),
                ('number_1', models.IntegerField()),
                ('number_2', models.IntegerField()),
                ('number_3', models.IntegerField()),
                ('number_4', models.IntegerField()),
                ('number_5', models.IntegerField()),
                ('number_6', models.IntegerField()),
                ('bonus_number', models.IntegerField()),
                ('div_winners_1', models.IntegerField()),
                ('div_winners_2', models.IntegerField()),
                ('div_winners_3', models.IntegerField()),
                ('div_winners_4', models.IntegerField()),
                ('div_winners_5', models.IntegerField()),
                ('div_winners_6', models.IntegerField()),
                ('div_winners_7', models.IntegerField()),
                ('div_winners_8', models.IntegerField()),
                ('div_prise_1', models.FloatField()),
                ('div_prise_2', models.FloatField()),
                ('div_prise_3', models.FloatField()),
                ('div_prise_4', models.FloatField()),
                ('div_prise_5', models.FloatField()),
                ('div_prise_6', models.FloatField()),
                ('div_prise_7', models.FloatField()),
                ('div_prise_8', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LottoP2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.CharField(max_length=50)),
                ('number_1', models.IntegerField()),
                ('number_2', models.IntegerField()),
                ('number_3', models.IntegerField()),
                ('number_4', models.IntegerField()),
                ('number_5', models.IntegerField()),
                ('number_6', models.IntegerField()),
                ('bonus_number', models.IntegerField()),
                ('div_winners_1', models.IntegerField()),
                ('div_winners_2', models.IntegerField()),
                ('div_winners_3', models.IntegerField()),
                ('div_winners_4', models.IntegerField()),
                ('div_winners_5', models.IntegerField()),
                ('div_winners_6', models.IntegerField()),
                ('div_winners_7', models.IntegerField()),
                ('div_winners_8', models.IntegerField()),
                ('div_prise_1', models.FloatField()),
                ('div_prise_2', models.FloatField()),
                ('div_prise_3', models.FloatField()),
                ('div_prise_4', models.FloatField()),
                ('div_prise_5', models.FloatField()),
                ('div_prise_6', models.FloatField()),
                ('div_prise_7', models.FloatField()),
                ('div_prise_8', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LottoP3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.CharField(max_length=50)),
                ('number_1', models.IntegerField()),
                ('number_2', models.IntegerField()),
                ('number_3', models.IntegerField()),
                ('number_4', models.IntegerField()),
                ('number_5', models.IntegerField()),
                ('number_6', models.IntegerField()),
                ('bonus_number', models.IntegerField()),
                ('div_winners_1', models.IntegerField()),
                ('div_winners_2', models.IntegerField()),
                ('div_winners_3', models.IntegerField()),
                ('div_winners_4', models.IntegerField()),
                ('div_winners_5', models.IntegerField()),
                ('div_winners_6', models.IntegerField()),
                ('div_winners_7', models.IntegerField()),
                ('div_winners_8', models.IntegerField()),
                ('div_prise_1', models.FloatField()),
                ('div_prise_2', models.FloatField()),
                ('div_prise_3', models.FloatField()),
                ('div_prise_4', models.FloatField()),
                ('div_prise_5', models.FloatField()),
                ('div_prise_6', models.FloatField()),
                ('div_prise_7', models.FloatField()),
                ('div_prise_8', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PowerBall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.CharField(max_length=50)),
                ('number_1', models.IntegerField()),
                ('number_2', models.IntegerField()),
                ('number_3', models.IntegerField()),
                ('number_4', models.IntegerField()),
                ('number_5', models.IntegerField()),
                ('bonus_number', models.IntegerField()),
                ('div_winners_1', models.IntegerField()),
                ('div_winners_2', models.IntegerField()),
                ('div_winners_3', models.IntegerField()),
                ('div_winners_4', models.IntegerField()),
                ('div_winners_5', models.IntegerField()),
                ('div_winners_6', models.IntegerField()),
                ('div_winners_7', models.IntegerField()),
                ('div_winners_8', models.IntegerField()),
                ('div_winners_9', models.IntegerField()),
                ('div_prise_1', models.FloatField()),
                ('div_prise_2', models.FloatField()),
                ('div_prise_3', models.FloatField()),
                ('div_prise_4', models.FloatField()),
                ('div_prise_5', models.FloatField()),
                ('div_prise_6', models.FloatField()),
                ('div_prise_7', models.FloatField()),
                ('div_prise_8', models.FloatField()),
                ('div_prise_9', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PowerBallP1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.CharField(max_length=50)),
                ('number_1', models.IntegerField()),
                ('number_2', models.IntegerField()),
                ('number_3', models.IntegerField()),
                ('number_4', models.IntegerField()),
                ('number_5', models.IntegerField()),
                ('bonus_number', models.IntegerField()),
                ('div_winners_1', models.IntegerField()),
                ('div_winners_2', models.IntegerField()),
                ('div_winners_3', models.IntegerField()),
                ('div_winners_4', models.IntegerField()),
                ('div_winners_5', models.IntegerField()),
                ('div_winners_6', models.IntegerField()),
                ('div_winners_7', models.IntegerField()),
                ('div_winners_8', models.IntegerField()),
                ('div_winners_9', models.IntegerField()),
                ('div_prise_1', models.FloatField()),
                ('div_prise_2', models.FloatField()),
                ('div_prise_3', models.FloatField()),
                ('div_prise_4', models.FloatField()),
                ('div_prise_5', models.FloatField()),
                ('div_prise_6', models.FloatField()),
                ('div_prise_7', models.FloatField()),
                ('div_prise_8', models.FloatField()),
                ('div_prise_9', models.FloatField()),
            ],
        ),
    ]
