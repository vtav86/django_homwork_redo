# Generated by Django 4.0.4 on 2022-04-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=64, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'in writing'), (2, 'pending editor approval'), (3, 'published')])),
                ('publish_date', models.DateField(null=True)),
                ('removal_date', models.DateField(null=True)),
            ],
        ),
    ]
