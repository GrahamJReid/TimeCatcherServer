# Generated by Django 4.1.3 on 2023-08-17 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('image_url', models.CharField(max_length=1000)),
                ('uid', models.CharField(max_length=10000)),
            ],
        ),
    ]
