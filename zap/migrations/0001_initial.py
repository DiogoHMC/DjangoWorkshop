# Generated by Django 4.2.4 on 2023-08-17 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tamanho', models.CharField(max_length=3)),
                ('preco', models.FloatField(max_length=9)),
            ],
        ),
    ]
