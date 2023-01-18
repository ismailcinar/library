# Generated by Django 4.0.4 on 2023-01-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_library', '0005_remove_book_date_created_remove_book_date_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='date_published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
