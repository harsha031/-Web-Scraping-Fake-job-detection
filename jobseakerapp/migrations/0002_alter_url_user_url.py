# Generated by Django 4.1.3 on 2022-12-10 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobseakerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='user_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_url', to='jobseakerapp.user'),
        ),
    ]
