# Generated by Django 2.2.7 on 2019-11-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
