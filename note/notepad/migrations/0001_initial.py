# Generated by Django 4.1.5 on 2023-01-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('heading', models.TextField(max_length=30)),
                ('text', models.TextField(max_length=1000)),
            ],
        ),
    ]
