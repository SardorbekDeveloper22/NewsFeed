# Generated by Django 4.0 on 2022-12-20 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0006_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='created_time',
        ),
    ]