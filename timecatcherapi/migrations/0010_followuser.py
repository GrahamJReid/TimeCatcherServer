# Generated by Django 4.1.3 on 2023-09-06 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timecatcherapi', '0009_collaborativetimelineevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followedUser', to='timecatcherapi.user')),
                ('followingUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followingUser', to='timecatcherapi.user')),
            ],
        ),
    ]
