# Generated by Django 4.1.3 on 2022-12-14 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0030_alter_vendor_vendoradded'),
    ]

    operations = [
        migrations.AddField(
            model_name='employ',
            name='departments',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
