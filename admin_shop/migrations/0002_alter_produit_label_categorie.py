# Generated by Django 4.0.4 on 2022-05-05 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='label_Categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_shop.categorie'),
        ),
    ]