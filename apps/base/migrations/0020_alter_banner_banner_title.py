# Generated by Django 5.0.3 on 2024-03-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_banner_id_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_title',
            field=models.CharField(max_length=20, verbose_name='Banner_title'),
        ),
    ]
