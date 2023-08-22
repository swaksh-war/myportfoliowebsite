# Generated by Django 4.2.2 on 2023-08-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default title', max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No data', max_length=255)),
                ('degree', models.CharField(default='No data', max_length=255)),
                ('started_year', models.PositiveIntegerField()),
                ('ender_year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='No data', max_length=255)),
                ('company_post', models.CharField(default='No data', max_length=255)),
                ('work_description', models.TextField()),
                ('started_from', models.DateField()),
                ('worked_till', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No data', max_length=255)),
                ('description', models.TextField()),
                ('started_date', models.DateField()),
                ('ended_date', models.DateField()),
            ],
        ),
    ]