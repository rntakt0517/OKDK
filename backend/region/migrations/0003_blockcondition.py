# Generated by Django 4.2.18 on 2025-02-06 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0002_block_selected_robot'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateTimeField(auto_now=True)),
                ('condition', models.FloatField()),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.block')),
            ],
        ),
    ]
