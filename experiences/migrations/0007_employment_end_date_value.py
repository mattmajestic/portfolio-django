# Generated by Django 3.2 on 2022-07-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0006_alter_employment_current_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employment',
            name='end_date_value',
            field=models.CharField(blank=True, max_length=255, verbose_name='End Date'),
        ),
    ]
