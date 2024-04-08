# Generated by Django 5.0.1 on 2024-01-30 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_alter_customer_doc_upload_alter_customer_photo'),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.gender'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.designation'),
        ),
    ]
