# Generated by Django 5.0.3 on 2024-03-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_alter_footer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampage',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]