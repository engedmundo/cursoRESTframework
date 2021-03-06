# Generated by Django 4.0.3 on 2022-03-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_alter_rating_options'),
        ('comments', '0002_alter_comment_options'),
        ('attractions', '0003_alter_attraction_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='comment',
            field=models.ManyToManyField(blank=True, null=True, to='comments.comment', verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='rating',
            field=models.ManyToManyField(blank=True, null=True, to='ratings.rating', verbose_name='Avaliação'),
        ),
    ]
