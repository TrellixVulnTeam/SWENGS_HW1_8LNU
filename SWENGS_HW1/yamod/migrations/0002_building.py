# Generated by Django 2.2.7 on 2019-11-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('color', models.TextField()),
            ],
        ),
    ]