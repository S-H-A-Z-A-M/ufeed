# Generated by Django 4.0 on 2022-03-16 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufeed', '0003_sign_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=17)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]