# Generated by Django 4.0.4 on 2022-05-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0008_allsongs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allsongs',
            options={'verbose_name_plural': 'Songs'},
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='exercises_app.category'),
        ),
    ]