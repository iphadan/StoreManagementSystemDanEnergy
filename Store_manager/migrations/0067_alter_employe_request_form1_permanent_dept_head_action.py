# Generated by Django 4.1.3 on 2023-01-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0066_alter_employe_request_form1_permanent_store_keeper_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe_request_form1_permanent',
            name='dept_head_Action',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=200, null=True),
        ),
    ]