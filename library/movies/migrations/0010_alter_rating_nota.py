# Generated by Django 4.1.7 on 2023-03-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_remove_movies_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='nota',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=3),
        ),
    ]
