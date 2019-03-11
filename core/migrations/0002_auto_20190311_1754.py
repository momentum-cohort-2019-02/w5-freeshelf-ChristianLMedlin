# Generated by Django 2.1.7 on 2019-03-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books_authored',
            field=models.ManyToManyField(help_text='Names of all the books this author has contributed to', null=True, to='core.Book'),
        ),
    ]
