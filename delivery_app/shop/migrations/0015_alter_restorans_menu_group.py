# Generated by Django 4.2.1 on 2023-05-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_restorans_menu_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restorans_menu',
            name='group',
            field=models.CharField(choices=[('PapaJoe', 'PapaJoe'), ('Kfc', 'Kfc'), ('McDonalds', 'McDonalds'), ('etc', 'etc')], default='McDonalds', max_length=20),
        ),
    ]
