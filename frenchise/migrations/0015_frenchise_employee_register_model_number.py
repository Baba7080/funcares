# Generated by Django 4.2.4 on 2023-10-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frenchise', '0014_profilefrenchise_partner_at_revenue'),
    ]

    operations = [
        migrations.AddField(
            model_name='frenchise_employee_register_model',
            name='number',
            field=models.IntegerField(blank=True, default='2', max_length=10),
        ),
    ]