# Generated by Django 5.0.3 on 2024-03-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='pintrest',
        ),
        migrations.AddField(
            model_name='team',
            name='pinterest',
            field=models.URLField(default=1, verbose_name='Pinterest'),
            preserve_default=False,
        ),
    ]
