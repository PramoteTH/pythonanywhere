# Generated by Django 2.2.7 on 2020-09-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_importplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='intravel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('nameplace', models.CharField(max_length=200)),
                ('namewrite', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=1000)),
                ('rating', models.IntegerField(default=0, max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='importplace',
        ),
    ]
