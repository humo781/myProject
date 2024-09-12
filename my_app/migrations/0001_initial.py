# Generated by Django 5.1.1 on 2024-09-12 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('pages', models.IntegerField()),
                ('language', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
    ]
