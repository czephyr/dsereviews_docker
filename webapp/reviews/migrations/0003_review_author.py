# Generated by Django 3.2.12 on 2022-07-23 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_auto_20220723_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='is_author', to='auth.user'),
            preserve_default=False,
        ),
    ]
