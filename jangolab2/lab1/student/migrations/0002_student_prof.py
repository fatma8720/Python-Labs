# Generated by Django 5.0.4 on 2024-04-28 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='prof',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prof.prof'),
            preserve_default=False,
        ),
    ]
