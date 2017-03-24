# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_quotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(11)]),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quoted_by',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(4)], max_length=255),
        ),
    ]
