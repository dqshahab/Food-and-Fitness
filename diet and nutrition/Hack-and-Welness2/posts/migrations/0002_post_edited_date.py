# Generated by Django 4.0.7 on 2022-09-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited_date',
            field=models.DateTimeField(null=True),
        ),
    ]
