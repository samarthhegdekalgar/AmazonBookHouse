# Generated by Django 2.2.7 on 2019-11-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_auto_20191115_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
