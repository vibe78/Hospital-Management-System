# Generated by Django 2.2.6 on 2020-07-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0011_auto_20200724_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirm_drug',
            name='drug_name',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='confirm_drug',
            name='drug_price',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
