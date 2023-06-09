# Generated by Django 4.2 on 2023-04-26 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0008_product_quantity"),
        ("uaccount", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userfavoriteproducts",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite",
                to="products.product",
            ),
        ),
        migrations.AlterField(
            model_name="userfavoriteproducts",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
