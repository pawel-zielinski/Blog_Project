# Generated by Django 3.1.6 on 2021-04-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['publish_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment_date']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=255),
        ),
    ]
