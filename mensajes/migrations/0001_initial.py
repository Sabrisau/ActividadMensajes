# Generated by Django 4.2 on 2024-08-27 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('remitente', models.CharField(max_length=200)),
                ('destinatario', models.CharField(max_length=200)),
                ('fecha_envio', models.DateTimeField()),
            ],
        ),
    ]
