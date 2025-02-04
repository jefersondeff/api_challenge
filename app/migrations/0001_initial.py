# Generated by Django 3.1 on 2020-08-06 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.CharField(max_length=300, verbose_name='Descrição')),
                ('auth', models.CharField(max_length=100, verbose_name='Autor')),
                ('number_page', models.IntegerField(verbose_name='Numero de páginas')),
                ('status', models.CharField(choices=[('Disponível', 'Disponível'), ('Emprestado', 'Emprestado')], max_length=100, verbose_name='Status')),
                ('date_reserved', models.DateField(blank=True, null=True, verbose_name='Data reserva')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
