# Generated by Django 4.0.4 on 2022-06-23 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0002_groupmodel_ledgermodel_remove_ledger_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contra',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountled', to='tallyapp.ledgermodel'),
        ),
        migrations.AlterField(
            model_name='contra',
            name='particulars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partled', to='tallyapp.ledgermodel'),
        ),
    ]
