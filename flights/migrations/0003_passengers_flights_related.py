# Generated by Django 4.1.1 on 2023-01-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_passengers'),
    ]

    operations = [
        migrations.AddField(
            model_name='passengers',
            name='flights_related',
            field=models.ManyToManyField(blank=True, related_name='passengers_related', to='flights.flight'),
        ),
    ]
