# Generated by Django 3.0.7 on 2020-06-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='', upload_to='articles/'),
            preserve_default=False,
        ),
    ]