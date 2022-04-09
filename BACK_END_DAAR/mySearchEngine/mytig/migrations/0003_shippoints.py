# Generated by Django 4.0.3 on 2022-03-08 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytig', '0002_auto_20201204_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tigID', models.IntegerField(default='-1')),
            ],
            options={
                'ordering': ('tigID',),
            },
        ),
    ]
