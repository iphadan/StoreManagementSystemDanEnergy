# Generated by Django 4.1.3 on 2022-12-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0052_alter_form2permanent_add_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='Type_of_Asset',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
