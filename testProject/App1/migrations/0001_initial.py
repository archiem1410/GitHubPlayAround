# Generated by Django 2.0.2 on 2018-02-23 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app_1',
            fields=[
                ('native_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('email_id', models.CharField(default='archimedha@mailinator.com', max_length=100)),
            ],
        ),
    ]
