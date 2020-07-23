# Generated by Django 3.0.8 on 2020-07-21 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=66)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
