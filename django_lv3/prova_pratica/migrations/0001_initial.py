# Generated by Django 4.1.3 on 2022-11-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messaggio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contatto', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('oggetto', models.CharField(max_length=100)),
                ('contenuto', models.TextField()),
            ],
        ),
    ]
