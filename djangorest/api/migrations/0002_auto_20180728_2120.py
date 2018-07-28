# Generated by Django 2.0.7 on 2018-07-28 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='awards',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='boxoffice',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='country',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='director',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='dvd',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='genre',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='imdbID',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='imdbRating',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='imdbVotes',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='language',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='metascore',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='plot',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='poster',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='production',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='rated',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='ratings',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='website',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movielist',
            name='writer',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
