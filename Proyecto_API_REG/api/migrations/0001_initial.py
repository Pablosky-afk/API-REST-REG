# Generated by Django 3.2.4 on 2021-11-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=10)),
            ],
        ),
    ]
