# Generated by Django 2.2.6 on 2020-07-31 09:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0013_auto_20200729_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='send_report_to_pharmacy',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='send_report_to_pharmacy',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
