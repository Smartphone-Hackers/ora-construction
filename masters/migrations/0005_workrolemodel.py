# Generated by Django 3.1 on 2020-09-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0004_workcategorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkRoleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workrole', models.CharField(max_length=100)),
            ],
        ),
    ]
