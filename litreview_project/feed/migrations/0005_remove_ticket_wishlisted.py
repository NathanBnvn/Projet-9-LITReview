# Generated by Django 3.2.4 on 2021-07-11 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_ticket_wishlisted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='wishlisted',
        ),
    ]