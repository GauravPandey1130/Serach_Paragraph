# Generated by Django 5.0.2 on 2024-04-16 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search_paragraph_logic', '0002_paragraph_wordindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Search_paragraph_logic.paragraph')),
            ],
        ),
    ]
