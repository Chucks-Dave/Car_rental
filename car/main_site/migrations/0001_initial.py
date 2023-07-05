# Generated by Django 3.2a1 on 2022-07-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_panel', '0007_auto_20220722_1240'),
        ('user', '0003_alter_user_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_location', models.CharField(max_length=500, verbose_name='Pick up Location (optional)')),
                ('pick_up_date', models.DateTimeField()),
                ('drop_off_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='user.user')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='admin_panel.vehicle')),
            ],
        ),
    ]