# Generated by Django 3.2.12 on 2022-05-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='updated',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='password',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]