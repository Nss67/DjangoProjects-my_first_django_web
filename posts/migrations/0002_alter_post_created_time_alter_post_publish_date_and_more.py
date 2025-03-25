# Generated by Django 5.1.7 on 2025-03-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
