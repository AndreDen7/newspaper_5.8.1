# Generated by Django 4.1.2 on 2022-11-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_delete_showpost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('NEWS', 'Новость'), ('ARTICLE', 'Статья')], default='AR', max_length=7),
        ),
    ]
