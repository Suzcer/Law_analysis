# Generated by Django 4.0 on 2022-01-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_remove_lawdocument_uisagain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawdocument',
            name='vother',
        ),
        migrations.RemoveField(
            model_name='lawdocument',
            name='vtext',
        ),
        migrations.AddField(
            model_name='lawdocument',
            name='vjson',
            field=models.JSONField(default={}, verbose_name='json数据'),
        ),
        migrations.AlterField(
            model_name='lawdocument',
            name='uage',
            field=models.CharField(max_length=32, null=True, verbose_name='出生年月'),
        ),
        migrations.AlterField(
            model_name='lawdocument',
            name='ugender',
            field=models.CharField(max_length=32, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='lawdocument',
            name='unation',
            field=models.CharField(max_length=32, null=True, verbose_name='民族'),
        ),
        migrations.AlterField(
            model_name='lawdocument',
            name='uplace',
            field=models.CharField(max_length=64, null=True, verbose_name='出生地'),
        ),
    ]
