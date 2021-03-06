# Generated by Django 4.0.3 on 2022-03-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listOFBooks',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddConstraint(
            model_name='listofbooks',
            constraint=models.UniqueConstraint(fields=('title', 'id'), name='unique'),
        ),
    ]
