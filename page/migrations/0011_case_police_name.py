# Generated by Django 2.0.3 on 2018-03-28 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='police_name',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
