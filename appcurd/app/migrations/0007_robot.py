# Generated by Django 4.0 on 2021-12-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_female'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full', models.CharField(max_length=40)),
                ('man', models.CharField(max_length=40)),
                ('sem', models.CharField(max_length=40)),
            ],
        ),
    ]
