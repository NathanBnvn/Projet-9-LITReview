# Generated by Django 3.2.4 on 2021-07-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0004_book_ticket_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ticket_id',
            field=models.IntegerField(blank=True),
        ),
    ]
