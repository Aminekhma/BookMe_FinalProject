# Generated by Django 4.0.3 on 2022-03-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygutenberg', '0009_alter_listofbooks_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofbooks',
            name='language',
            field=models.CharField(default='', max_length=5),
        ),
    ]
