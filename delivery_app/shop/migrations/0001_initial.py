# Generated by Django 4.2.1 on 2023-05-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restoran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
