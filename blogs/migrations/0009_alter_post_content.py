# Generated by Django 3.2 on 2022-07-25 11:23

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_delete_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=mdeditor.fields.MDTextField(blank=True, verbose_name='Content'),
        ),
    ]
