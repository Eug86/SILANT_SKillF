# Generated by Django 4.2.3 on 2023-08-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip', '0002_typecmost_typemachine_typemotor_typetranc_typevmost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typecmost',
            name='name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='typemotor',
            name='name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='typetranc',
            name='name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='typevmost',
            name='name',
            field=models.CharField(max_length=16),
        ),
    ]
