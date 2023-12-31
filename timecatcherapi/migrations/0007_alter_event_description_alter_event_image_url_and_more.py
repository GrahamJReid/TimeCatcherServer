# Generated by Django 4.1.3 on 2023-09-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timecatcherapi', '0006_event_isprivate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
