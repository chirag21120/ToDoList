# Generated by Django 4.0.3 on 2022-03-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=30)),
                ('tskDesc', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
