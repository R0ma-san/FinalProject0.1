# Generated by Django 3.2.9 on 2021-12-16 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0006_auto_20211215_0406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='top_worldwide',
        ),
    ]
