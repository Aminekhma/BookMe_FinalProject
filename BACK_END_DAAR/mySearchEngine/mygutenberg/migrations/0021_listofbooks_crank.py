# Generated by Django 4.0.3 on 2022-03-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygutenberg', '0020_alter_bookgraphjaccard_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofbooks',
            name='crank',
            field=models.FloatField(default='0.0'),
        ),
    ]