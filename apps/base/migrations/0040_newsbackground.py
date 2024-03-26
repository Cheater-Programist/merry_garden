# Generated by Django 5.0.3 on 2024-03-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_alter_footer_options_remove_contactpost_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_background', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'News_Background',
                'verbose_name_plural': 'Workers_Backgrounds',
            },
        ),
    ]