# Generated by Django 3.2.7 on 2021-10-24 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('biofloc', '0002_build_tank'),
    ]

    operations = [
        migrations.AddField(
            model_name='build_tank',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
