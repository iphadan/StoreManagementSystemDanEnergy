# Generated by Django 4.1.3 on 2022-11-28 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0004_alter_catagory_total_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='total_item',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=200, null=True)),
                ('total_item_in_Stok', models.CharField(blank=True, default='0', max_length=200, null=True)),
                ('last_update', models.DateField(auto_now_add=True)),
                ('Catagory', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.catagory')),
            ],
        ),
    ]