# Generated by Django 2.1.7 on 2019-10-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0003_auto_20191013_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseinfo',
            name='cost',
            field=models.FloatField(),
        ),
    ]
