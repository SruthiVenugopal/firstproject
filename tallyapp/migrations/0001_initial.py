# Generated by Django 4.0.4 on 2022-06-20 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tallyapp.groups')),
            ],
        ),
        migrations.CreateModel(
            name='contra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('no', models.PositiveIntegerField()),
                ('amount', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='tallyapp.ledger')),
                ('particulars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='particulars', to='tallyapp.ledger')),
            ],
        ),
    ]