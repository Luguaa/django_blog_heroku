# Generated by Django 2.0 on 2020-05-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='article.Tag', verbose_name='标签'),
        ),
    ]
