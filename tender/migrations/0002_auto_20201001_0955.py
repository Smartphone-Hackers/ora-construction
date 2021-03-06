# Generated by Django 3.1 on 2020-10-01 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0007_worknamemodel'),
        ('tender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderdetails',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.customermodel'),
        ),
        migrations.AlterField(
            model_name='tenderdetails',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.departmentmodel'),
        ),
    ]
