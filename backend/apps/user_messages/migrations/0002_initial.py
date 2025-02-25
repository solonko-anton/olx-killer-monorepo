# Generated by Django 5.1 on 2024-12-09 10:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('user_messages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmessage',
            name='history_user',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='historicalmessage',
            name='recipient',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to=settings.AUTH_USER_MODEL,
                verbose_name='The recipient of the message',
            ),
        ),
        migrations.AddField(
            model_name='historicalmessage',
            name='sender',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to=settings.AUTH_USER_MODEL,
                verbose_name='The sender of the message',
            ),
        ),
        migrations.AddField(
            model_name='message',
            name='parent',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='replies',
                to='user_messages.message',
            ),
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='received_messages',
                to=settings.AUTH_USER_MODEL,
                verbose_name='The recipient of the message',
            ),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='sent_messages',
                to=settings.AUTH_USER_MODEL,
                verbose_name='The sender of the message',
            ),
        ),
        migrations.AddField(
            model_name='historicalmessage',
            name='parent',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to='user_messages.message',
            ),
        ),
        migrations.AddField(
            model_name='messageimage',
            name='message',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='message_images', to='user_messages.message'
            ),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['sender'], name='user_messag_sender__d1a1bb_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['recipient'], name='user_messag_recipie_b62633_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['parent'], name='user_messag_parent__8c6cdf_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['updated_at'], name='user_messag_updated_88e44f_idx'),
        ),
    ]
