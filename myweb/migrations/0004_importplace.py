# Generated by Django 2.2.7 on 2020-09-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_auto_20200918_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='importplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlimg', models.CharField(max_length=200)),
                ('nameimg', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0, max_length=10)),
            ],
        ),
    ]
