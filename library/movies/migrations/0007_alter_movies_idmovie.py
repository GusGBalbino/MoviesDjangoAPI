# Generated by Django 4.1.7 on 2023-03-04 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movies_nota_delete_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='idMovie',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
