# Generated by Django 3.0.4 on 2020-04-07 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('domain', models.CharField(max_length=64)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(help_text='without @', max_length=32)),
                ('realname', models.CharField(blank=True, max_length=64, null=True)),
                ('password', models.CharField(max_length=500)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vmails.Domain')),
            ],
            options={
                'unique_together': {('username', 'domain')},
            },
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('alias', models.CharField(help_text='without @', max_length=32)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('mailbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vmails.Mailbox')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
