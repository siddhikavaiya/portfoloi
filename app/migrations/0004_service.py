# Generated by Django 3.2.8 on 2021-10-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211029_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('desc', models.TextField()),
            ],
        ),
    ]