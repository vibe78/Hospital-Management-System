# Generated by Django 2.2.6 on 2020-07-22 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0004_send_report_to_pharmacy_medical'),
    ]

    operations = [
        migrations.AddField(
            model_name='medical_test',
            name='Book_Apointment_mo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Book_Apointment', to='doc.Book_Apointment_model'),
        ),
    ]
