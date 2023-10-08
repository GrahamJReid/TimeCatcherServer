# Generated by Django 4.1.3 on 2023-09-07 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timecatcherapi', '0014_delete_followthread'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowThread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timecatcherapi.thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timecatcherapi.user')),
            ],
        ),
    ]