# Generated by Django 4.1.7 on 2023-03-04 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_avaliacao_delete_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='nota',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.DeleteModel(
            name='Avaliacao',
        ),
    ]
