# Generated by Django 2.1 on 2018-09-16 20:21

from django.db import migrations, models
import phonenumber_field.modelfields


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
                ('celular', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Celular')),
                ('cargo', models.CharField(blank='True', max_length=120, verbose_name='Cargo')),
                ('empresa', models.CharField(blank='True', max_length=50, verbose_name='Empresa')),
                ('email', models.EmailField(blank='True', max_length=120, verbose_name='Email')),
            ],
        ),
    ]
