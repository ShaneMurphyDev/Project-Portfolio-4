# Generated by Django 3.2.23 on 2023-11-21 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('natureblog', '0002_subscription'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]