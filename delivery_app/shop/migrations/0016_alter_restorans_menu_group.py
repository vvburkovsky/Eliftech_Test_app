# Generated by Django 4.2.1 on 2023-05-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_restorans_menu_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restorans_menu',
            name='group',
            field=models.CharField(choices=[('etc', 'etc'), ('PapaJoe', 'PapaJoe'), ('Kfc', 'Kfc'), ('McDonalds', 'McDonalds')], default='McDonalds', max_length=20),
        ),
    ]
