# Generated by Django 3.2.12 on 2022-07-24 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='professor',
        ),
        migrations.AddField(
            model_name='review',
            name='professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_professor', to='reviews.professor'),
            preserve_default=False,
        ),
    ]
