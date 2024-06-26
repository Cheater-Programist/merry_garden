# Generated by Django 5.0.3 on 2024-03-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_facilties_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team', verbose_name='Image')),
                ('fullname', models.CharField(max_length=100, verbose_name='Full name')),
                ('job', models.CharField(max_length=100, verbose_name='Job')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('pintrest', models.URLField(verbose_name='Pintrest')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
