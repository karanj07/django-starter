# Generated by Django 4.0.4 on 2022-07-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngos', '0006_school_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='schools/'),
        ),
    ]