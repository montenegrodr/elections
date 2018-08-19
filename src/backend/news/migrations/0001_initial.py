# Generated by Django 2.1 on 2018-08-18 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('body', models.TextField(null=True)),
                ('source', models.CharField(max_length=255, null=True)),
                ('source_url', models.CharField(max_length=255, null=True)),
                ('author', models.CharField(max_length=255, null=True)),
                ('facebook', models.IntegerField(null=True)),
                ('googleplus', models.IntegerField(null=True)),
                ('linkedin', models.IntegerField(null=True)),
                ('published_at', models.DateTimeField()),
                ('permalink', models.CharField(max_length=1000, null=True)),
                ('canonical', models.CharField(max_length=1000, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=255)),
                ('last_searched_at', models.DateTimeField(default=None, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Candidate')),
            ],
        ),
    ]