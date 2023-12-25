# Generated by Django 5.0 on 2023-12-25 05:43

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='recipes_cat_name_0c4a4b_idx')],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(default=None, null=True)),
                ('ingredients', models.TextField(default=None, null=True)),
                ('steps', models.TextField()),
                ('time_cook', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('photo', models.ImageField(default=None, null=True, upload_to='img/')),
                ('categories', models.ManyToManyField(to='recipes.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
                'indexes': [models.Index(fields=['title'], name='recipes_rec_title_9ebae8_idx')],
            },
        ),
    ]
