# Generated by Django 4.0.3 on 2022-03-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('opening_hours', models.TextField(verbose_name='Horário de funcionamento')),
                ('minimum_age', models.IntegerField(verbose_name='Idade mínima')),
            ],
        ),
    ]
