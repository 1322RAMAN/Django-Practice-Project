# Generated by Django 4.2.17 on 2024-12-17 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('publish_blog', 'Can publish blog'), ('archive_blog', 'Can archive blog')]},
        ),
    ]