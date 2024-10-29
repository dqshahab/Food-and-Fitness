# Generated by Django 4.0.7 on 2022-09-24 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('Breakfast', 'BF'), ('Lunch', 'L'), ('Dinner', 'D')], max_length=100)),
                ('plate', models.TextField()),
            ],
        ),
    ]
