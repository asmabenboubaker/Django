# Generated by Django 4.1.5 on 2023-02-07 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_alter_event_eventdate_alter_event_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePart', models.DateField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('person', 'event')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='participate',
            field=models.ManyToManyField(related_name='participations', through='events.Participation', to=settings.AUTH_USER_MODEL),
        ),
    ]
