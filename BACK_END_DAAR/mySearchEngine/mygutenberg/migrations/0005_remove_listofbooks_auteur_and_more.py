# Generated by Django 4.0.3 on 2022-03-09 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygutenberg', '0004_remove_listofbooks_unique_listofbooks_unique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listofbooks',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='coverBook',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='language',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='text',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='value',
        ),
    ]