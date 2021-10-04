# Generated by Django 3.2.7 on 2021-10-03 18:28

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211003_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=16)),
                ('code_2', models.CharField(max_length=2)),
                ('code_3', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='language',
            field=models.CharField(default='EN', max_length=3),
        ),
        migrations.AlterField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(on_delete=models.SET(api.models.get_sentinel_user), to='api.profile'),
        ),
    ]
