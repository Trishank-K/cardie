# Generated by Django 5.0.3 on 2024-06-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='background_color',
        ),
        migrations.RemoveField(
            model_name='card',
            name='layout',
        ),
        migrations.RemoveField(
            model_name='card',
            name='link_info',
        ),
        migrations.RemoveField(
            model_name='card',
            name='text_info',
        ),
        migrations.RemoveField(
            model_name='card',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='card',
            name='user_pronouns',
        ),
        migrations.AddField(
            model_name='card',
            name='data',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='card',
            name='uuid',
            field=models.CharField(default='', max_length=36),
        ),
    ]
