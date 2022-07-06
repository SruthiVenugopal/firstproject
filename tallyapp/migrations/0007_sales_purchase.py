# Generated by Django 4.0.4 on 2022-07-05 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0006_journal_narration'),
    ]

    operations = [
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narration', models.CharField(max_length=30)),
                ('transactiontype', models.CharField(choices=[('cheque/dd', 'Cheque/dd'), ('atm', 'Atm'), ('card', 'Card'), ('cash', 'Cash'), ('e-fund-transfer', 'E-fund-transfer'), ('others', 'Others')], default='cheque/dd', max_length=30)),
                ('instno', models.PositiveIntegerField(default=5656)),
                ('instdate', models.CharField(default='24Mar2022', max_length=255)),
                ('date', models.DateField(auto_now=True)),
                ('no', models.PositiveIntegerField(default=0)),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salacc', to='tallyapp.ledger')),
                ('particulars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salled', to='tallyapp.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narration', models.CharField(max_length=30)),
                ('transactiontype', models.CharField(choices=[('cheque/dd', 'Cheque/dd'), ('atm', 'Atm'), ('card', 'Card'), ('cash', 'Cash'), ('e-fund-transfer', 'E-fund-transfer'), ('others', 'Others')], default='cheque/dd', max_length=30)),
                ('instno', models.PositiveIntegerField(default=5656)),
                ('instdate', models.CharField(default='24Mar2022', max_length=255)),
                ('date', models.DateField(auto_now=True)),
                ('no', models.PositiveIntegerField(default=0)),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='puracc', to='tallyapp.ledger')),
                ('particulars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purled', to='tallyapp.ledger')),
            ],
        ),
    ]