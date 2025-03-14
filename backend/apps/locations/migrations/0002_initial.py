# Generated by Django 5.1.6 on 2025-03-02 11:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalcity',
            name='history_user',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='historicallocation',
            name='city',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to='locations.city',
                verbose_name='City',
            ),
        ),
        migrations.AddField(
            model_name='historicallocation',
            name='history_user',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='historicalregion',
            name='history_user',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='locations.city',
                verbose_name='City',
            ),
        ),
        migrations.AddField(
            model_name='historicalcity',
            name='region',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to='locations.region',
                verbose_name='Region',
            ),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='cities',
                to='locations.region',
                verbose_name='Region',
            ),
        ),
        migrations.AddField(
            model_name='village',
            name='region',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='villages',
                to='locations.region',
                verbose_name='Region',
            ),
        ),
        migrations.AddField(
            model_name='location',
            name='village',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='locations.village',
                verbose_name='Village',
            ),
        ),
        migrations.AddField(
            model_name='historicallocation',
            name='village',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to='locations.village',
                verbose_name='Village',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('name', 'region')},
        ),
        migrations.AlterUniqueTogether(
            name='village',
            unique_together={('name', 'region')},
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('latitude', 'longitude')},
        ),
    ]
