# Generated by Django 3.0.6 on 2020-06-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20200617_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=models.TextField(),
        ),
    ]