# Generated by Django 5.1.7 on 2025-03-19 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('updated_At', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
