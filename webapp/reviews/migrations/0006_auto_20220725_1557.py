# Generated by Django 3.2.12 on 2022-07-25 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220724_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='emoji',
            field=models.CharField(choices=[('Indifferent', '😐'), ('Loved it', '😍'), ('Hated it', '🙁')], max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='examStars',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='lectureStars',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
