# Generated by Django 5.0.1 on 2024-03-10 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0007_my_tier_lists_my_watched_movies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tier_list_watched_movies',
            name='tier_ranking_row',
            field=models.TextField(),
        ),
    ]