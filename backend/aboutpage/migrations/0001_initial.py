# Generated by Django 5.0.6 on 2024-05-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=23)),
                ('specialization', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
