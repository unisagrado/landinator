# Generated by Django 3.1.3 on 2020-11-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201116_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='accept',
            field=models.BooleanField(default=False, verbose_name='termos aceitos?'),
        ),
    ]