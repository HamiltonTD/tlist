# Generated by Django 4.2.7 on 2023-12-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_item_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='favorite',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]