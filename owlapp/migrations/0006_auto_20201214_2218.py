# Generated by Django 3.1.4 on 2020-12-14 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owlapp', '0005_auto_20201214_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='case',
            name='questionnumber',
            field=models.IntegerField(),
        ),
    ]
