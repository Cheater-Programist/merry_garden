# Generated by Django 5.0.3 on 2024-03-26 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_banner_banner_text_banner_banner_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Footer Info', 'verbose_name_plural': 'Footer Infos'},
        ),
        migrations.RemoveField(
            model_name='contactpost',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='footerpost',
            name='footer',
        ),
    ]
