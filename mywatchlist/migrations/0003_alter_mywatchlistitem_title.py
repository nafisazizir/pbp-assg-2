# Generated by Django 4.1 on 2022-09-28 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_rename_mywatchlist_mywatchlistitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlistitem',
            name='title',
            field=models.TextField(),
        ),
    ]