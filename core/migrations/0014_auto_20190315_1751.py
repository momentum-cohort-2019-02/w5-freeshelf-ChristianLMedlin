# Generated by Django 2.1.7 on 2019-03-15 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190315_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_slug',
            field=models.SlugField(),
        ),
    ]
