# Generated by Django 4.2.6 on 2023-12-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_article_image_alter_article_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name="Makale'ye Fotograf Ekle"),
        ),
    ]
