# Generated by Django 3.1 on 2022-01-12 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAccount',
            new_name='UserProfile',
        ),
    ]
