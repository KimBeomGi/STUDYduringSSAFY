# Generated by Django 3.2.18 on 2023-03-24 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('audience', models.IntegerField(blank=True)),
                ('release_date', models.DateField(null=True)),
                ('genre', models.CharField(max_length=30)),
                ('score', models.FloatField(null=True)),
                ('poster_url', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('actor_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
