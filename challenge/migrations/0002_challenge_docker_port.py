# Generated by Django 4.0.4 on 2023-03-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='docker_port',
            field=models.IntegerField(default=8000),
            preserve_default=False,
        ),
    ]