# Generated by Django 4.0.3 on 2022-03-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygutenberg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofbooks',
            name='auteur',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='listofbooks',
            name='coverBook',
            field=models.CharField(default='', max_length=355),
        ),
        migrations.AddField(
            model_name='listofbooks',
            name='language',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='listofbooks',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='listofbooks',
            name='value',
            field=models.FloatField(default='0.0'),
        ),
    ]
