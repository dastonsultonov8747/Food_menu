# Generated by Django 5.1.4 on 2024-12-10 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=600, upload_to='bigmenu/')),
            ],
        ),
        migrations.CreateModel(
            name='SmallMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=600, upload_to='smallmenu/')),
                ('bigmenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.bigmenu')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(max_length=600, upload_to='product/')),
                ('smallmenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.smallmenu')),
            ],
        ),
    ]
