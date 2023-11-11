# Generated by Django 4.2.4 on 2023-10-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companystaff', '0004_alter_loan_creation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demat_account',
            name='created',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='created',
        ),
        migrations.RemoveField(
            model_name='mutual_fund',
            name='created',
        ),
        migrations.AddField(
            model_name='demat_account',
            name='creation',
            field=models.DateField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='insurance',
            name='creation',
            field=models.DateField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='mutual_fund',
            name='creation',
            field=models.DateField(max_length=8, null=True),
        ),
    ]