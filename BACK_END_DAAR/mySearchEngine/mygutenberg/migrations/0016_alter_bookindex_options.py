# Generated by Django 4.0.3 on 2022-03-09 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygutenberg', '0015_alter_bookindex_wordocc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookindex',
            options={'ordering': ['idBook', 'wordOcc']},
        ),
    ]
