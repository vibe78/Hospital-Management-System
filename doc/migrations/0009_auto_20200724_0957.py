# Generated by Django 2.2.6 on 2020-07-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0008_auto_20200724_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='send_report_to_pharmacy',
            name='Pham',
        ),
        migrations.AddField(
            model_name='send_report_to_pharmacy',
            name='medical',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medical', to='doc.Medical_test'),
        ),
    ]
