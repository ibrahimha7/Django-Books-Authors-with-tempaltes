# Generated by Django 2.2.5 on 2019-09-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
