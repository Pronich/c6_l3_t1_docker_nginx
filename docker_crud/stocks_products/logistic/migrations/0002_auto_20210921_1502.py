# Generated by Django 3.2.5 on 2021-09-21 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['address'], 'verbose_name': 'склад', 'verbose_name_plural': 'склады'},
        ),
        migrations.AlterModelOptions(
            name='stockproduct',
            options={'verbose_name': 'Товар на склад', 'verbose_name_plural': 'Товар на складе'},
        ),
    ]
