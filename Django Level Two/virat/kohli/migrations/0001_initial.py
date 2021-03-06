# Generated by Django 2.1.7 on 2019-03-30 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kohli.Company')),
            ],
        ),
        migrations.AddField(
            model_name='money',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kohli.Webpage'),
        ),
    ]
