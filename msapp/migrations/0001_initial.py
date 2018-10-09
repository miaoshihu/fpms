# Generated by Django 2.0.7 on 2018-10-09 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=10)),
                ('price', models.CharField(default='面议', max_length=10, unique=True)),
                ('viewtimes', models.PositiveIntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modify_time', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '二手物品',
                'verbose_name_plural': '二手物品列表',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, unique=True)),
                ('icon', models.CharField(blank=True, default=None, max_length=50)),
                ('phoneno', models.CharField(blank=True, default=None, max_length=50)),
                ('login_times', models.PositiveSmallIntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modify_time', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户列表',
            },
        ),
        migrations.AddField(
            model_name='good',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='msapp.User'),
        ),
    ]
