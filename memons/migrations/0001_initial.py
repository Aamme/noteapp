# Generated by Django 3.0.6 on 2020-05-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('streetno', models.CharField(max_length=50)),
                ('postalcode', models.CharField(max_length=50)),
            ],
        ),
    ]
