# Generated by Django 4.0.4 on 2022-04-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.IntegerField(choices=[(-1, 'not defined'), (0, 'rock'), (1, 'metal'), (2, 'pop'), (3, 'hip-hop'), (4, 'electronic'), (5, 'reggae'), (6, 'other')], default=-1),
        ),
        migrations.AddField(
            model_name='band',
            name='still_active',
            field=models.BooleanField(default=True),
        ),
    ]
