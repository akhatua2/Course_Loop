# Generated by Django 3.1 on 2020-08-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davematthews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrqAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.IntegerField(default=10)),
                ('keywords', models.CharField(default='-', max_length=100)),
            ],
        ),
    ]