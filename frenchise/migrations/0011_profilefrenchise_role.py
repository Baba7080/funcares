# Generated by Django 4.2.4 on 2023-10-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frenchise', '0010_frenchise_employee_register_model_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefrenchise',
            name='Role',
            field=models.CharField(default='employee', max_length=120),
        ),
    ]
