# Generated by Django 5.0.7 on 2024-12-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('OTP', models.CharField(max_length=6)),
                ('type_of_user', models.CharField(max_length=10)),
            ],
        ),
    ]