# Generated by Django 4.2.6 on 2023-12-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_options_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name="Makale'ye Fotograf Ekle"),
        ),
    ]