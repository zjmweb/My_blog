# Generated by Django 3.0.6 on 2020-06-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_eduexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='selfcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
    ]