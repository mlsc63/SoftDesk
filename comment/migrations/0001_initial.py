# Generated by Django 3.2 on 2021-05-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]