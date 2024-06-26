# Generated by Django 5.0.1 on 2024-01-31 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docters', '0003_rename_createat_refdoctor_refcreateat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refdoctor',
            name='refaddress',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='refdoctor',
            name='refcountry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='refdoctor',
            name='refemail',
            field=models.EmailField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='refdoctor',
            name='refmobile',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='refdoctor',
            name='refphone',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='refdoctor',
            name='refpincode',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='refdoctor',
            name='refpricelist',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='refdoctor',
            name='refregister',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='refdoctor',
            name='refspeciality',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='refdoctor',
            name='refstate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
