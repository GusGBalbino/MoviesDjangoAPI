# Generated by Django 4.1.7 on 2023-03-04 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_movies_idmovie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nota', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('idMovie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movies')),
            ],
        ),
    ]
