# Generated by Django 3.0.6 on 2020-06-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_interest_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='eduexperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('start', models.CharField(max_length=10)),
                ('end', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
