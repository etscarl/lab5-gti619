# Generated by Django 2.0.7 on 2018-07-18 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameField', models.CharField(max_length=16)),
                ('passwordField', models.CharField(max_length=256)),
            ],
        ),
    ]