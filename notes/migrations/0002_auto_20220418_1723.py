# Generated by Django 3.2.6 on 2022-04-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='noteDesc',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='noteTitle',
            field=models.CharField(max_length=255),
        ),
    ]
