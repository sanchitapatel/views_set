# Generated by Django 5.0.8 on 2024-08-08 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'MovieModel',
                'verbose_name_plural': 'MovieModels',
            },
        ),
    ]
