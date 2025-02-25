# Generated by Django 4.2.2 on 2023-06-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "imageapp",
            "0012_register_address_register_country_register_pincode_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="register",
            name="Address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="register",
            name="Country",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="register",
            name="Pincode",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="register",
            name="State",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="register",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="register",
            name="phoneno",
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
