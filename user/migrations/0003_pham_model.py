# Generated by Django 2.2.6 on 2020-07-18 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_category_ph'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pham_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=500)),
                ('Other_name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('image', models.ImageField(default='T.png', upload_to='profile_pic')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.category_ph')),
            ],
        ),
    ]
