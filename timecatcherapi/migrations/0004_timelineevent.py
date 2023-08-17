# Generated by Django 4.1.3 on 2023-08-17 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timecatcherapi', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelineEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timecatcherapi.event')),
                ('timeline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timecatcherapi.timeline')),
            ],
        ),
    ]
