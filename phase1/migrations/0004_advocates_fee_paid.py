# Generated by Django 4.1.4 on 2023-07-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase1', '0003_advocates_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocates',
            name='fee_paid',
            field=models.BooleanField(default=False),
        ),
    ]