# Generated by Django 4.0 on 2022-01-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_lawdocument_uage_lawdocument_ugender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawdocument',
            name='uage',
            field=models.CharField(default='1900', max_length=32, verbose_name='出生年月'),
        ),
        migrations.AlterField(
            model_name='lawdocument',
            name='ugender',
            field=models.CharField(default='男', max_length=32, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='lawdocument',
            name='uname',
            field=models.CharField(default='无名氏', max_length=32, verbose_name='犯罪嫌疑人'),
        ),
        migrations.AlterField(
            model_name='lawdocument',
            name='unation',
            field=models.CharField(default='汉族', max_length=32, verbose_name='民族'),
        ),
        migrations.AlterField(
            model_name='lawdocument',
            name='uplace',
            field=models.CharField(default='中国', max_length=64, verbose_name='出生地'),
        ),
        migrations.AlterField(
            model_name='lawdocument',
            name='vtime',
            field=models.IntegerField(default=1900, verbose_name='审判时间'),
        ),
    ]
