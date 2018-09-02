# Generated by Django 2.1 on 2018-09-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('celular', models.IntegerField(verbose_name='Celular')),
                ('cargo', models.CharField(max_length=120, verbose_name='Cargo')),
                ('empresa', models.CharField(max_length=50, verbose_name='Empresa')),
                ('email', models.EmailField(max_length=120, verbose_name='Email')),
            ],
        ),
    ]