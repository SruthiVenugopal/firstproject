# Generated by Django 4.0.4 on 2022-07-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0005_contra_narration_receipt_payment_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='narration',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
