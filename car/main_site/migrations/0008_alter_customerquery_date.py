# Generated by Django 3.2a1 on 2022-07-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_auto_20220726_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerquery',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]