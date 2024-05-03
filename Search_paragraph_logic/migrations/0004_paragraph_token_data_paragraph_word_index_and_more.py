# Generated by Django 5.0.2 on 2024-04-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search_paragraph_logic', '0003_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='token_data',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='word_index',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='text',
            field=models.JSONField(default=dict),
        ),
    ]
