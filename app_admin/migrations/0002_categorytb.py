# Generated by Django 3.2.12 on 2024-01-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
    ]