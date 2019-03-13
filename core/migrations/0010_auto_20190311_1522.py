# Generated by Django 2.1.7 on 2019-03-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_programming_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='programming_language',
        ),
        migrations.AddField(
            model_name='book',
            name='programming_language',
            field=models.ManyToManyField(blank=True, help_text='Select the appropriate programming language', to='core.Programming_Languages'),
        ),
        migrations.RemoveField(
            model_name='programming_languages',
            name='language',
        ),
        migrations.AddField(
            model_name='programming_languages',
            name='language',
            field=models.CharField(help_text='Enter the programming language this book covers', max_length=50, null=True),
        ),
    ]
