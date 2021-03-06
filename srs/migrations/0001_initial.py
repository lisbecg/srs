# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-11 20:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('audio', models.FileField(upload_to='audio/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_directory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_directory', to='srs.Directory')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equation', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('label', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('hiddenField', models.TextField(blank=True, null=True)),
                ('activate', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('keywords', models.TextField(null=True)),
                ('label', models.TextField(null=True)),
                ('body', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('directory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.Directory')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='videos/%Y/%m/%d/')),
                ('thumbnail', models.ImageField(upload_to='thumbnails/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('notecard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.Notecard')),
            ],
        ),
        migrations.AddField(
            model_name='notecard',
            name='notefile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srs.Notefile'),
        ),
        migrations.AddField(
            model_name='image',
            name='notecard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.Notecard'),
        ),
        migrations.AddField(
            model_name='equation',
            name='notecard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.Notecard'),
        ),
        migrations.AddField(
            model_name='document',
            name='notecard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.Notecard'),
        ),
        migrations.AddField(
            model_name='audio',
            name='notecard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.Notecard'),
        ),
    ]
