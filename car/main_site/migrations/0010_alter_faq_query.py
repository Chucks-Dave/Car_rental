# Generated by Django 3.2a1 on 2022-07-26 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0009_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq', to='main_site.customerquery'),
        ),
    ]